from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_get_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "Information": "Too see all available methods visit /docs page"
    }
