from fastapi.testclient import TestClient

from app import app
from config import ADMIN_NICKNAME, ADMIN_PASSWORD

client = TestClient(app)


def test_get_classes():
    response = client.get("/heroclasses")
    assert response.status_code == 200


def test_get_class():
    response = client.get("/heroclass?class_name=Воїн")
    assert response.status_code == 200


def test_post_class():
    token_response = client.post(
        "/login", data={"username": ADMIN_NICKNAME, "password": ADMIN_PASSWORD}
    )
    access_token = token_response.json()["access_token"]
    response = client.post(
        "/heroclass",
        json={
            "name": "Воїн2",
            "characteristics": {
                "strength": 0,
                "agility": 0,
                "intuition": 0,
                "intelligence": 0,
            },
            "choices": 0,
        },
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 201


def test_update_class():
    token_response = client.post(
        "/login", data={"username": ADMIN_NICKNAME, "password": ADMIN_PASSWORD}
    )
    access_token = token_response.json()["access_token"]
    response = client.put(
        "/heroclass?class_name=Воїн2",
        json={
            "characteristics": {
                "strength": 2,
            }
        },
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 200


def test_delete_class():
    token_response = client.post(
        "/login", data={"username": ADMIN_NICKNAME, "password": ADMIN_PASSWORD}
    )
    access_token = token_response.json()["access_token"]
    response = client.delete(
        "/heroclass?class_name=Воїн2",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 204
