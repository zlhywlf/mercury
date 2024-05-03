from dataclasses import asdict

from models.Fake import fake_config
from models.StarletteContext import StarletteContext


def test_hello_world(ctx: StarletteContext):
    """"""
    response = ctx.client.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello": "world"}


async def test_add_rds_config(ctx: StarletteContext):
    """"""
    tbl_name = ctx.setting.rds_task_table_name
    await ctx.db.drop_collection(tbl_name)
    ret = await ctx.db[tbl_name].insert_many([asdict(_) for _ in fake_config])
    assert ret.acknowledged


def test_rds_by_get(ctx: StarletteContext):
    """"""
    response = ctx.client.get("/rds", params={"appId": "table01", "a": "a_str", "b": "b_str", **ctx.rds_auth})
    assert response.status_code == 200


def test_rds_by_post(ctx: StarletteContext):
    """"""
    response = ctx.client.post("/rds", params=ctx.rds_auth, json={"appId": "table01", "a": "a_str", "b": "b_str", })
    assert response.status_code == 200


def test_rds_new_task(ctx: StarletteContext):
    """"""
    response = ctx.client.post("/rds", json={
        "appId": "userInfo",
        "a": "a_str",
        "b": "b_str",
        **ctx.rds_auth
    })
    assert response.status_code == 200
