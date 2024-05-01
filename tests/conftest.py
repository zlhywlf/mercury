from collections.abc import Generator
from typing import Any

from pytest import fixture
from starlette.applications import Starlette
from starlette.testclient import TestClient

from mercury.main import starlette_app


@fixture()
def starlette_app_() -> Generator[Starlette, Any, None]:
    """"""
    yield starlette_app.app


@fixture()
def starlette_client(starlette_app_: Starlette) -> TestClient:
    """"""
    return TestClient(starlette_app_)
