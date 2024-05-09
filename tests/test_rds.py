from .mocks.fakes.tasks.SimpleTask import simple_task
from .models.TestContext import TestContext


async def test_hello_world(ctx: TestContext):
    """"""
    response = await ctx.client.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello": "world"}


async def test_simple_task(ctx: TestContext):
    """"""
    response = await ctx.client.post(
        "/rds", json={"appId": simple_task._id, "arg": "simple_task_response_200", **ctx.rds_auth}
    )
    assert response.status_code == 200
