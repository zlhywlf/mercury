from starlette.testclient import TestClient


def test_hello_world(starlette_client: TestClient) -> None:
    """"""
    response = starlette_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello": "world"}
