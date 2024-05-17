from tests.models.TestContext import TestContext


async def test_homepage(ctx: TestContext):
    """"""
    response = await ctx.client.get("/")
    assert response.status_code == 200
    assert response.json() == {"hostname": "127.0.0.1"}
