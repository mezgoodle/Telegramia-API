from fastapi.testclient import TestClient

from app import app
from config import ADMIN_NICKNAME, ADMIN_PASSWORD

client = TestClient(app)


def test_get_raids():
    response = client.get("/raids")
    assert response.status_code == 200


def test_get_raid():
    response = client.get("/raid?name=Dungeon")
    assert response.status_code == 200


def test_post_raid():
    token_response = client.post(
        "/login", data={"username": ADMIN_NICKNAME, "password": ADMIN_PASSWORD}
    )
    access_token = token_response.json()["access_token"]
    response = client.post(
        "/raid",
        json={
            "name": "dungeon",
            "description": "dungeon",
            "damage": 1231.213,
            "base_time": 133,
            "treasure": 12312.323,
            "members": {"mezgoodle": "2008-09-15T15:53:00+05:00"},
        },
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 201


def test_update_raid():
    token_response = client.post(
        "/login", data={"username": ADMIN_NICKNAME, "password": ADMIN_PASSWORD}
    )
    access_token = token_response.json()["access_token"]
    response = client.put(
        "/raid?name=dungeon",
        json={"damage": 346},
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 200


def test_delete_raid():
    token_response = client.post(
        "/login", data={"username": ADMIN_NICKNAME, "password": ADMIN_PASSWORD}
    )
    access_token = token_response.json()["access_token"]
    response = client.delete(
        "/raid?name=dungeon", headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 204
