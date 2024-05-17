from tests.mocks.tasks.SimpleApi import simple_api
from tests.mocks.tasks.SimpleSubject import simple_subject
from tests.mocks.tasks.SimpleTable import simple_table
from tests.models.TestContext import TestContext


async def test_simple_api(ctx: TestContext):
    """"""
    data = {"appId": simple_api._id, "arg": "simple_api_response_200", "index": 1, "size": 10, **ctx.auth}
    response = await ctx.client.post("/rds", json=data)
    assert response.status_code == 200


async def test_simple_table(ctx: TestContext):
    """"""
    data = {"appId": simple_table._id, "arg": "simple_api_response_200", **ctx.auth}
    response = await ctx.client.post("/rds", json=data)
    assert response.status_code == 200


async def test_simple_subject(ctx: TestContext):
    """"""
    data = {
        "appId": simple_subject._id,
        "subject_arg": "simple_api_response_200",
        "subject01": "s001",
        "subject02": "s002",
        **ctx.auth,
    }
    response = await ctx.client.post("/rds", json=data)
    assert response.status_code == 200
