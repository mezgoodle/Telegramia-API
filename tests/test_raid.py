from fastapi.testclient import TestClient

from app import app
from config import ADMIN_NICKNAME, ADMIN_PASSWORD

client = TestClient(app)


def test_get_raids():
    response = client.get("/raids")
    assert response.status_code == 200


def test_get_raidlevels():
    response = client.get("/raidlevels?raid_name=raid")
    assert response.status_code == 200


def test_get_raid():
    response = client.get("/raid?raid_name=raid")
    assert response.status_code == 200


def test_post_raid():
    token_response = client.post(
        "/login", data={"username": ADMIN_NICKNAME, "password": ADMIN_PASSWORD}
    )
    access_token = token_response.json()["access_token"]
    response = client.post(
        "/raid",
        json={
            "name": "Raid",
            "description": "raid",
            "members": {"mezgoodle": {"time": "2008-09-15T15:53:00+05:00", "level": 1}},
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
        "/raid?raid_name=Raid",
        json={"description": "346"},
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 200


def test_delete_raid():
    token_response = client.post(
        "/login", data={"username": ADMIN_NICKNAME, "password": ADMIN_PASSWORD}
    )
    access_token = token_response.json()["access_token"]
    response = client.delete(
        "/raid?raid_name=Raid", headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 204
