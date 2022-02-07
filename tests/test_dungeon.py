from fastapi.testclient import TestClient

from app import app
from config import ADMIN_NICKNAME, ADMIN_PASSWORD

client = TestClient(app)


def test_get_dungeons():
    response = client.get('/dungeons')
    assert response.status_code == 200


def test_get_dungeon():
    response = client.get('/dungeon?dungeon_name=dungeon')
    assert response.status_code == 200


def test_post_dungeon():
    token_response = client.post(
        '/login',
        data={'username': ADMIN_NICKNAME, 'password': ADMIN_PASSWORD})
    access_token = token_response.json()['access_token']
    response = client.post(
        '/dungeon',
        json={
            'name': 'dungeon',
            'description': 'dungeon',
            'damage': 1231.213,
            'base_time': 133,
            'treasure': 12312.323,
            'members': {'mezgoodle': '2008-09-15'}
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
        '/dungeon?dungeon_name=dungeon',
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
        '/dungeon?dungeon_name=dungeon',
        headers={'Authorization': f'Bearer {access_token}'}
    )
    assert response.status_code == 204
