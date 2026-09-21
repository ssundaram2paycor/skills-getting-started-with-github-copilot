from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_root_redirects_to_static_index():
    response = client.get("/", follow_redirects=False)

    assert response.status_code in {302, 307}
    assert response.headers["location"] == "/static/index.html"


def test_hello_world_endpoint_returns_message():
    response = client.get("/hello")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}
