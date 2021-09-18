from fastapi.testclient import TestClient

from app import app
from config import ADMIN_NICKNAME, ADMIN_PASSWORD

client = TestClient(app)


def test_get_roads():
    response = client.get('/roads')
    assert response.status_code == 200


def test_get_road():
    response = client.get('/road?name=Дорога на захід')
    assert response.status_code == 200


def test_post_road():
    token_response = client.post(
        '/login',
        data={'username': ADMIN_NICKNAME, 'password': ADMIN_PASSWORD})
    access_token = token_response.json()['access_token']
    response = client.post(
        '/road',
        json={
            "name": "Big forest route",
            "from_obj": "Ogrimmar",
            "to_obj": "Stormwind",
            "energy": "13.4"
        },
        headers={'Authorization': f'Bearer {access_token}'}
    )
    assert response.status_code == 201


def test_update_road():
    token_response = client.post(
        '/login',
        data={'username': ADMIN_NICKNAME, 'password': ADMIN_PASSWORD})
    access_token = token_response.json()['access_token']
    response = client.put(
        '/road?name=Big forest route',
        json={
            "intelligence": 346
        },
        headers={'Authorization': f'Bearer {access_token}'}
    )
    assert response.status_code == 200


def test_delete_road():
    token_response = client.post(
        '/login',
        data={'username': ADMIN_NICKNAME, 'password': ADMIN_PASSWORD})
    access_token = token_response.json()['access_token']
    response = client.delete(
        '/road?name=Big forest route',
        headers={'Authorization': f'Bearer {access_token}'}
    )
    assert response.status_code == 204
