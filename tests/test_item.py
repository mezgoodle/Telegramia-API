from fastapi.testclient import TestClient

from app import app
from config import ADMIN_NICKNAME, ADMIN_PASSWORD

client = TestClient(app)


def test_get_items():
    response = client.get("/items")
    assert response.status_code == 200


def test_get_item():
    response = client.get("/item?item_name=Wood helmet&city_name=Брісвель")
    assert response.status_code == 200


def test_post_item():
    token_response = client.post(
        "/login", data={"username": ADMIN_NICKNAME, "password": ADMIN_PASSWORD}
    )
    access_token = token_response.json()["access_token"]
    response = client.post(
        "/item",
        json={
            "name": "Wood helmet1",
            "characteristic": "strength",
            "type": "helmet",
            "bonus": 13.3,
            "city": "Stormwind",
            "price": 34,
            "count": 0,
        },
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 201


def test_update_item():
    token_response = client.post(
        "/login", data={"username": ADMIN_NICKNAME, "password": ADMIN_PASSWORD}
    )
    access_token = token_response.json()["access_token"]
    response = client.put(
        "/item?item_name=Wood helmet1&city_name=Stormwind",
        json={"bonus": 181.3123},
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 200


def test_delete_item():
    token_response = client.post(
        "/login", data={"username": ADMIN_NICKNAME, "password": ADMIN_PASSWORD}
    )
    access_token = token_response.json()["access_token"]
    response = client.delete(
        "/item?item_name=Wood helmet1&city_name=Stormwind",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 204
