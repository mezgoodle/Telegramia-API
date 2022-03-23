from fastapi.testclient import TestClient

from app import app
from config import ADMIN_NICKNAME, ADMIN_PASSWORD

client = TestClient(app)


def test_get_countries():
    response = client.get("/countries")
    assert response.status_code == 200


def test_get_country():
    response = client.get("/country?capital=Брісвель")
    assert response.status_code == 200


def test_post_country():
    token_response = client.post(
        "/login", data={"username": ADMIN_NICKNAME, "password": ADMIN_PASSWORD}
    )
    access_token = token_response.json()["access_token"]
    response = client.post(
        "/country",
        json={
            "name": "Priaria",
            "description": "Big country",
            "capital": "Stormwind",
            "population": 0,
        },
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 201


def test_update_country():
    token_response = client.post(
        "/login", data={"username": ADMIN_NICKNAME, "password": ADMIN_PASSWORD}
    )
    access_token = token_response.json()["access_token"]
    response = client.put(
        "/country?country_name=Priaria",
        json={"population": 100},
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 200


def test_delete_country():
    token_response = client.post(
        "/login", data={"username": ADMIN_NICKNAME, "password": ADMIN_PASSWORD}
    )
    access_token = token_response.json()["access_token"]
    response = client.delete(
        "/country?country_name=Priaria",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 204
