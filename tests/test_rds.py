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
    await ctx.db.drop_collection("rds_config")
    ret = await ctx.db["rds_config"].insert_many([asdict(_) for _ in fake_config])
    assert ret.acknowledged


def test_rds_by_get(ctx: StarletteContext):
    """"""
    response = ctx.client.get("/rds", params={"appId": "table01", **ctx.rds_auth})
    assert response.status_code == 200


def test_rds_by_post(ctx: StarletteContext):
    """"""
    response = ctx.client.post("/rds", params=ctx.rds_auth, json={"appId": "table01"})
    assert response.status_code == 200


def test_rds_new_task(ctx: StarletteContext):
    """"""
    ctx.client.post("/rds", json={
        "appId": "table01",
        **ctx.rds_auth
    })
