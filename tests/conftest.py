import os
from typing import Any, Generator

from models.StarletteContext import StarletteContext
from pytest import fixture
from starlette.testclient import TestClient

from mercury.app import app


@fixture(scope="session")
def ctx() -> Generator[StarletteContext, Any, None]:
    os.chdir(os.path.join(os.path.dirname(__file__), ".."))
    with TestClient(app) as client:
        yield StarletteContext(client=client,
                               rds_auth={"userId": "test-user",
                                         "userKey": "2b9119ecd2676e197d714d8510b02e7d"},
                               db=app.context.mongo_client,
                               setting=app.setting)


@fixture(autouse=True)
def anyio_backend() -> str:
    return 'asyncio'
