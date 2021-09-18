from fastapi.testclient import TestClient

from app import app
from config import ADMIN_NICKNAME, ADMIN_PASSWORD

client = TestClient(app)


def test_get_horses():
    response = client.get('/horses')
    assert response.status_code == 404


def test_get_horse():
    response = client.get('/horse?horse_name=Воїн')
    assert response.status_code == 404


def test_post_horse():
    token_response = client.post(
        '/login',
        data={'username': ADMIN_NICKNAME, 'password': ADMIN_PASSWORD})
    access_token = token_response.json()['access_token']
    response = client.post(
        '/horse',
        json={
            "name": "White faster",
            "bonus": 13.3,
            "city": "Stormwind",
            "price": 34
        },
        headers={'Authorization': f'Bearer {access_token}'}
    )
    assert response.status_code == 201


def test_update_horse():
    token_response = client.post(
        '/login',
        data={'username': ADMIN_NICKNAME, 'password': ADMIN_PASSWORD})
    access_token = token_response.json()['access_token']
    response = client.put(
        '/horse?horse_name=White faster',
        json={
            "price": 100
        },
        headers={'Authorization': f'Bearer {access_token}'}
    )
    assert response.status_code == 200


def test_delete_horse():
    token_response = client.post(
        '/login',
        data={'username': ADMIN_NICKNAME, 'password': ADMIN_PASSWORD})
    access_token = token_response.json()['access_token']
    response = client.delete(
        '/horse?horse_name=White faster',
        headers={'Authorization': f'Bearer {access_token}'}
    )
    assert response.status_code == 204
