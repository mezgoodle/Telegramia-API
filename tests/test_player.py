from fastapi.testclient import TestClient

from app import app
from config import ADMIN_NICKNAME, ADMIN_PASSWORD

client = TestClient(app)


def test_get_players():
    response = client.get("/players")
    assert response.status_code == 200


def test_get_player():
    response = client.get("/player?username=sylvenis")
    assert response.status_code == 200


def test_post_player():
    token_response = client.post(
        "/login", data={"username": ADMIN_NICKNAME, "password": ADMIN_PASSWORD}
    )
    access_token = token_response.json()["access_token"]
    response = client.post(
        "/player",
        json={
            "user_id": "34344334",
            "telegram_name": "mezgoodle",
            "name": "Jane Doe",
            "level": 3,
            "experience": 45,
            "health": 100,
            "energy": 30,
            "strength": 11.4,
            "agility": 3.2,
            "intuition": 55.1,
            "intelligence": 34,
            "hero_class": "paladin",
            "nation": "Priaria",
            "money": 123.65,
            "items": ["wood shield", "helmet"],
            "mount": {"name": "Bob", "type": "horse", "bonus": 12},
            "current_state": "Stormwind",
        },
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 201


def test_update_player():
    token_response = client.post(
        "/login", data={"username": ADMIN_NICKNAME, "password": ADMIN_PASSWORD}
    )
    access_token = token_response.json()["access_token"]
    response = client.put(
        "/player?nickname=Jane Doe",
        json={"intelligence": 346},
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 200


def test_delete_player():
    token_response = client.post(
        "/login", data={"username": ADMIN_NICKNAME, "password": ADMIN_PASSWORD}
    )
    access_token = token_response.json()["access_token"]
    response = client.delete(
        "/player?nickname=Jane Doe", headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 204
