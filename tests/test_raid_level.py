from fastapi.testclient import TestClient

from app import app
from config import ADMIN_NICKNAME, ADMIN_PASSWORD

client = TestClient(app)


def test_get_raid_levels():
    response = client.get("/raid_levels")
    assert response.status_code == 200


def test_get_raid_level():
    response = client.get("/raid_level?name=raid_level")
    assert response.status_code == 200


def test_post_raid_level():
    token_response = client.post(
        "/login", data={"username": ADMIN_NICKNAME, "password": ADMIN_PASSWORD}
    )
    access_token = token_response.json()["access_token"]
    response = client.post(
        "/raid_level",
        json={
            "name": "raid_level1",
            "raid_name": "raid",
            "description": "dungeon",
            "damage": 1231.213,
            "base_time": 133,
        },
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 201


def test_update_raid_level():
    token_response = client.post(
        "/login", data={"username": ADMIN_NICKNAME, "password": ADMIN_PASSWORD}
    )
    access_token = token_response.json()["access_token"]
    response = client.put(
        "/raid_level?name=raid_level1",
        json={"damage": 346},
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 200


def test_delete_raid_level():
    token_response = client.post(
        "/login", data={"username": ADMIN_NICKNAME, "password": ADMIN_PASSWORD}
    )
    access_token = token_response.json()["access_token"]
    response = client.delete(
        "/raid_level?name=raid_level1",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 204
