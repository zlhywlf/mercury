from models.Fake import api_user_info, app_user_info, fake_config
from models.StarletteContext import StarletteContext


async def test_hello_world(ctx: StarletteContext):
    """"""
    response = await ctx.client.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello": "world"}


async def test_add_rds_config(ctx: StarletteContext):
    """"""
    tbl_name = ctx.setting.rds_task_table_name
    db = await ctx.db.get_db_by_name(ctx.setting.project_name)
    await db.drop_collection(tbl_name)
    ret = await db[tbl_name].insert_many([_.model_dump() for _ in fake_config])
    assert ret.acknowledged


async def test_rds_by_get(ctx: StarletteContext):
    """"""
    response = await ctx.client.get("/rds",
                                    params={"appId": app_user_info._id, "aa": "a_str", "bb": "b_str", **ctx.rds_auth})
    assert response.status_code == 200


async def test_rds_by_post(ctx: StarletteContext):
    """"""
    response = await ctx.client.post("/rds",
                                     params=ctx.rds_auth,
                                     json={"appId": app_user_info._id, "aa": "a_str", "bb": "b_str", })
    assert response.status_code == 200


async def test_rds_new_task(ctx: StarletteContext):
    """"""
    response = await ctx.client.post("/rds", json={
        "appId": api_user_info._id,
        "a": "a_str",
        "b": "b_str",
        **ctx.rds_auth
    })
    assert response.status_code == 200
