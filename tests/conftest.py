import os
from typing import Any, Generator

from asgi_lifespan import LifespanManager
from httpx import ASGITransport, AsyncClient
from models.StarletteContext import StarletteContext
from pytest import fixture

from mercury.app import app


@fixture(scope="module")
async def ctx() -> Generator[StarletteContext, Any, None]:
    os.chdir(os.path.join(os.path.dirname(__file__), ".."))
    async with LifespanManager(app) as manager:
        async with AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://127.0.0.1:8000") as client:
            yield StarletteContext(client=client,
                                   rds_auth={"userId": "test-user",
                                             "userKey": "2b9119ecd2676e197d714d8510b02e7d"},
                                   db=app.context.mongo_client,
                                   setting=app.setting)


@fixture(scope="module", autouse=True)
def anyio_backend() -> str:
    return 'asyncio'
