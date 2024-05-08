import os
from typing import Any, Generator

from asgi_lifespan import LifespanManager
from httpx import ASGITransport, AsyncClient
from models.StarletteContext import StarletteContext
from pytest import fixture

from mercury.app import app
from mercury.utils.EncryptionUtil import encrypt_by_md5


@fixture(scope="module")
async def ctx() -> Generator[StarletteContext, Any, None]:
    os.chdir(os.path.join(os.path.dirname(__file__), ".."))
    user_id = "test-user"
    async with LifespanManager(app) as manager:
        async with AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://127.0.0.1:8000") as client:
            yield StarletteContext(client=client,
                                   rds_auth={"userId": user_id,
                                             "userKey": encrypt_by_md5(user_id + "+", app.context.setting.rds_key)},
                                   context=app.context)


@fixture(scope="module", autouse=True)
def anyio_backend() -> str:
    return 'asyncio'
