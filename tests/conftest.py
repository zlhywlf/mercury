import os
from typing import Any, Generator

from asgi_lifespan import LifespanManager
from httpx import ASGITransport, AsyncClient, MockTransport, Response
from mercury.__main__ import app
from mercury.app.utils import encrypt_by_md5
from mercury.rds.Service import Service
from pytest import fixture

from tests.mocks.HttpxMock import httpx_handle
from tests.mocks.MongoMock import MongoMock
from tests.mocks.tasks.SimpleApi import simple_api
from tests.mocks.tasks.SimpleSubject import simple_subject
from tests.mocks.tasks.SimpleTable import simple_table
from tests.models.TestContext import TestContext


async def response_hook(response: Response):
    pass


fake_tasks = [
    simple_api.model_dump(),
    simple_table.model_dump(),
    simple_subject.model_dump(),
]


@fixture(scope="module")
async def ctx() -> Generator[TestContext, Any, None]:
    os.chdir(os.path.join(os.path.dirname(__file__), ".."))
    user_id = "test-user"
    config = {
        "event_hooks": {"response": [response_hook]},
        "transport": MockTransport(httpx_handle),
    }
    app.context.http_client.client = AsyncClient(**config)
    app.context.mongo_client = MongoMock(app.context.setting)
    db = app.context.mongo_client.client[app.context.setting.project_name]
    await db[Service.TASK_TABLE_NAME].insert_many(fake_tasks)
    async with LifespanManager(app) as manager:
        async with AsyncClient(transport=ASGITransport(app=manager.app), base_url="http://127.0.0.1:8000") as client:
            yield TestContext(
                client=client,
                auth={
                    "userId": user_id,
                    "userKey": encrypt_by_md5(user_id + "+", app.context.setting.app_key),
                },
                context=app.context,
            )


@fixture(scope="module", autouse=True)
def anyio_backend() -> str:
    return "asyncio"
