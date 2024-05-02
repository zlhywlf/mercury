from models.StarletteContext import StarletteContext
from pytest import fixture
from starlette.testclient import TestClient

from mercury.main import create_starlette_app, create_async_db, create_setting


@fixture()
def ctx() -> StarletteContext:
    setting = create_setting()
    async_db = create_async_db(setting.mongo)
    app = create_starlette_app(setting, async_db)
    return StarletteContext(client=TestClient(app.instance),
                            rds_auth={"userId": "test-user",
                                      "userKey": "2b9119ecd2676e197d714d8510b02e7d"},
                            db=async_db)


@fixture(autouse=True)
def anyio_backend() -> str:
    return 'asyncio'
