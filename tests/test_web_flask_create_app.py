"""flask app 测试"""
from flask.testing import Client


def test_hello_world(flask_client: Client) -> None:
    """hello world 测试

    Args:
        flask_client: 客户端

    Returns: None

    """
    response = flask_client.get("/")
    assert b'Hello, World!' in response.data
