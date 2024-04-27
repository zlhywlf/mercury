"""pytest 全局对象"""

from collections.abc import Generator
from typing import Any

from flask import Flask
from flask.testing import FlaskClient
from pytest import fixture

from mercury.app.flask.create_app import app


@fixture(name="flask_app_")
def flask_app() -> Generator[Flask, Any, None]:
    """flask app 实例

    Yields:
        Generator[Flask, Any, None]: app 实例生成器
    """
    app.config.update(
        {
            "TESTING": True,
        }
    )
    yield app


@fixture()
def flask_client(flask_app_: Flask) -> FlaskClient:
    """flask client 实例

    Args:
        flask_app_ (Flask): flask 实例

    Returns:
        FlaskClient: flask 客户端
    """
    return flask_app_.test_client()
