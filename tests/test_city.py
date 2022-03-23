from fastapi.testclient import TestClient

from app import app
from config import ADMIN_NICKNAME, ADMIN_PASSWORD

client = TestClient(app)


def test_get_cities():
    response = client.get("/cities")
    assert response.status_code == 200


def test_get_city():
    response = client.get("/city?city_name=Брісвель")
    print(response.json())
    assert response.status_code == 200


def test_post_city():
    token_response = client.post(
        "/login", data={"username": ADMIN_NICKNAME, "password": ADMIN_PASSWORD}
    )
    access_token = token_response.json()["access_token"]
    response = client.post(
        "/city",
        json={
            "name": "Stormwind",
            "country": "Alliance",
            "is_capital": True,
            "market": True,
            "academy": False,
            "temple": False,
            "tavern": True,
            "menagerie": True,
        },
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 201


def test_update_city():
    token_response = client.post(
        "/login", data={"username": ADMIN_NICKNAME, "password": ADMIN_PASSWORD}
    )
    access_token = token_response.json()["access_token"]
    response = client.put(
        "/city?city_name=Stormwind",
        json={"market": False},
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 200


def test_delete_city():
    token_response = client.post(
        "/login", data={"username": ADMIN_NICKNAME, "password": ADMIN_PASSWORD}
    )
    access_token = token_response.json()["access_token"]
    response = client.delete(
        "/city?city_name=Stormwind", headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 204
