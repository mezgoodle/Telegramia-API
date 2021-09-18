from fastapi.testclient import TestClient

from app import app
from config import ADMIN_NICKNAME, ADMIN_PASSWORD

client = TestClient(app)


def test_get_admins():
    response = client.get('/admins')
    assert response.status_code == 200


def test_get_admin():
    response = client.get('/admin?admin_name=mezgoodle')
    assert response.status_code == 200


def test_post_admin():
    token_response = client.post(
        '/login',
        data={'username': ADMIN_NICKNAME, 'password': ADMIN_PASSWORD})
    access_token = token_response.json()['access_token']
    response = client.post(
        '/admin',
        json={
            "name": "mezgoodle",
            "email": "mezgoodle@gmail.com",
            "password": "123456"
        },
        headers={'Authorization': f'Bearer {access_token}'}
    )
    assert response.status_code == 201


def test_update_admin():
    token_response = client.post(
        '/login',
        data={'username': ADMIN_NICKNAME, 'password': ADMIN_PASSWORD})
    access_token = token_response.json()['access_token']
    response = client.put(
        '/admin?admin_name=mezgoodle',
        json={
            "name": "mezgoodle111"
        },
        headers={'Authorization': f'Bearer {access_token}'}
    )
    assert response.status_code == 200


def test_delete_admin():
    token_response = client.post(
        '/login',
        data={'username': ADMIN_NICKNAME, 'password': ADMIN_PASSWORD})
    access_token = token_response.json()['access_token']
    response = client.delete(
        '/admin?admin_name=mezgoodle',
        headers={'Authorization': f'Bearer {access_token}'}
    )
    assert response.status_code == 204
