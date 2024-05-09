from fakes.TaskFake import api_user_info, app_user_info
from models.TestContext import TestContext


async def test_hello_world(ctx: TestContext):
    """"""
    response = await ctx.client.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello": "world"}


async def test_rds_by_get(ctx: TestContext):
    """"""
    response = await ctx.client.get("/rds",
                                    params={"appId": app_user_info._id, "aa": "a_str", "bb": "b_str", **ctx.rds_auth})
    assert response.status_code == 200


async def test_rds_by_post(ctx: TestContext):
    """"""
    response = await ctx.client.post("/rds",
                                     params=ctx.rds_auth,
                                     json={"appId": app_user_info._id, "aa": "a_str", "bb": "b_str", })
    assert response.status_code == 200


async def test_rds_new_task(ctx: TestContext):
    """"""
    response = await ctx.client.post("/rds", json={
        "appId": api_user_info._id,
        "a": "a_str",
        "b": "b_str",
        **ctx.rds_auth
    })
    assert response.status_code == 200
