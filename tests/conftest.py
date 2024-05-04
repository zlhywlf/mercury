from typing import Any, Generator

from models.StarletteContext import StarletteContext
from motor.motor_asyncio import AsyncIOMotorClient
from pytest import fixture
from starlette.testclient import TestClient

from mercury.app import app
from mercury.settings.StarletteSetting import StarletteSetting


@fixture()
def ctx() -> Generator[StarletteContext, Any, None]:
    setting = StarletteSetting()
    async_db = AsyncIOMotorClient(setting.mongo)["mercury"]
    with TestClient(app) as client:
        yield StarletteContext(client=client,
                               rds_auth={"userId": "test-user",
                                         "userKey": "2b9119ecd2676e197d714d8510b02e7d"},
                               db=async_db,
                               setting=setting)


@fixture(autouse=True)
def anyio_backend() -> str:
    return 'asyncio'
