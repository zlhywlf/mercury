"""pytest 全局对象"""
from pytest import fixture
from flask import Flask
from flask.testing import Client
from mercury.web.flask.create_app import app


@fixture()
def flask_app() -> Flask:
    """flask app 实例"""
    app.config.update({
        "TESTING": True,
    })
    yield app


@fixture()
def flask_client(flask_app: Flask) -> Client:
    """flask client 实例"""
    return flask_app.test_client()
