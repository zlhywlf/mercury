import os
from typing import Any, Generator

from asgi_lifespan import LifespanManager
from fakes.TaskFake import task_data
from httpx import ASGITransport, AsyncClient, MockTransport
from mocks.HttpxMock import HttpxMock
from mocks.MongoMock import MongoMock
from models.TestContext import TestContext
from pytest import fixture

from mercury.app import app
from mercury.utils.EncryptionUtil import encrypt_by_md5


@fixture(scope="module")
async def ctx() -> Generator[TestContext, Any, None]:
    os.chdir(os.path.join(os.path.dirname(__file__), ".."))
    user_id = "test-user"
    app.context.http_client.client = AsyncClient(transport=MockTransport(HttpxMock()))
    app.context.mongo_client = MongoMock(app.context.setting)
    db = await app.context.mongo_client.get_db_by_name(app.context.setting.project_name)
    await db[app.context.setting.rds_task_table_name].insert_many(task_data)
    async with LifespanManager(app) as manager:
        async with AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://127.0.0.1:8000") as client:
            yield TestContext(client=client,
                              rds_auth={"userId": user_id,
                                        "userKey": encrypt_by_md5(user_id + "+", app.context.setting.rds_key)},
                              context=app.context)


@fixture(scope="module", autouse=True)
def anyio_backend() -> str:
    return 'asyncio'
