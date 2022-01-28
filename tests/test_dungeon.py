from fastapi.testclient import TestClient

from app import app
from config import ADMIN_NICKNAME, ADMIN_PASSWORD

client = TestClient(app)


def test_get_dungeons():
    response = client.get('/dungeons')
    assert response.status_code == 200


def test_get_dungeon():
    response = client.get('/dungeon?name=dungeon')
    assert response.status_code == 200


def test_post_dungeon():
    token_response = client.post(
        '/login',
        data={'username': ADMIN_NICKNAME, 'password': ADMIN_PASSWORD})
    access_token = token_response.json()['access_token']
    response = client.post(
        '/dungeon',
        json={
            "name": "dungeon",
            "description": "Підземелля Девіона",
            "damage": "1000.23",
            "base_time": "2s",
            "treasure": "2323.22",
            "members": {'mezgoodle': '1s'}
        },
        headers={'Authorization': f'Bearer {access_token}'}
    )
    assert response.status_code == 201


def test_update_dungeon():
    token_response = client.post(
        '/login',
        data={'username': ADMIN_NICKNAME, 'password': ADMIN_PASSWORD})
    access_token = token_response.json()['access_token']
    response = client.put(
        '/dungeon?name=dungeon',
        json={
            "damage": 346
        },
        headers={'Authorization': f'Bearer {access_token}'}
    )
    assert response.status_code == 200


def test_delete_dungeon():
    token_response = client.post(
        '/login',
        data={'username': ADMIN_NICKNAME, 'password': ADMIN_PASSWORD})
    access_token = token_response.json()['access_token']
    response = client.delete(
        '/dungeon?name=dungeon',
        headers={'Authorization': f'Bearer {access_token}'}
    )
    assert response.status_code == 204
