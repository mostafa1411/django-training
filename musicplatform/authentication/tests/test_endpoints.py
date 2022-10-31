import pytest
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_register_valid_user():
    user = {
        'username': 'mostafa_abdullah',
        'email': 'ma@gmail.com',
        'password1': 'pass123',
        'password2': 'pass123'
    }

    client = APIClient()
    response = client.post('/authentication/register/', user)
    data = response.data

    assert response.status_code == status.HTTP_201_CREATED
    assert 'token' in data
    assert 'id' in data['user']
    assert 'bio' in data['user']
    assert data['user']['username'] == user['username']
    assert data['user']['email'] == user['email']


@pytest.mark.django_db
def test_register_user_with_an_existing_username():
    user1 = {
        'username': 'mostafa_abdullah',
        'email': 'ma@gmail.com',
        'password1': 'pass123',
        'password2': 'pass123'
    }

    user2 = {
        'username': 'mostafa_abdullah',
        'email': 'ma2@gmail.com',
        'password1': 'pass456',
        'password2': 'pass456'
    }

    client = APIClient()
    client.post('/authentication/register/', user1)
    response = client.post('/authentication/register/', user2)

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_register_user_with_an_existing_email():
    user1 = {
        'username': 'mostafa_abdullah',
        'email': 'ma@gmail.com',
        'password1': 'pass123',
        'password2': 'pass123'
    }

    user2 = {
        'username': 'mostafa_abdullah2',
        'email': 'ma@gmail.com',
        'password1': 'pass456',
        'password2': 'pass456'
    }

    client = APIClient()
    client.post('/authentication/register/', user1)
    response = client.post('/authentication/register/', user2)

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_register_user_with_missing_username():
    user = {
        'email': 'ma@gmail.com',
        'password1': 'pass123',
        'password2': 'pass123'
    }

    client = APIClient()
    response = client.post('/authentication/register/', user)

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_register_with_missing_email():
    user = {
        'username': 'mostafa_abdullah',
        'password1': 'pass123',
        'password2': 'pass123'
    }

    client = APIClient()
    response = client.post('/authentication/register/', user)

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_register_user_with_non_matching_passwords():
    user = {
        'username': 'mostafa_abdullah',
        'email': 'ma@gmail.com',
        'password1': 'pass123',
        'password2': 'pass456'
    }

    client = APIClient()
    response = client.post('/authentication/register/', user)

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_login_valid_user():
    user = {
        'username': 'mostafa_abdullah',
        'email': 'ma@gmail.com',
        'password1': 'pass123',
        'password2': 'pass123'
    }

    login_data = {
        'username': 'mostafa_abdullah',
        'password': 'pass123'
    }

    client = APIClient()
    client.post('/authentication/register/', user)
    response = client.post('/authentication/login/', login_data)
    data = response.data

    assert response.status_code == status.HTTP_200_OK
    assert 'token' in data
    assert 'id' in data['user']
    assert 'bio' in data['user']
    assert data['user']['username'] == user['username']
    assert data['user']['email'] == user['email']


@pytest.mark.django_db
def test_login_non_existing_user():
    login_data = {
        'username': 'mostafa_abdullah',
        'password': 'pass123'
    }

    client = APIClient()
    response = client.post('/authentication/login/', login_data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_valid_logout(auth_client):
    client = auth_client()
    response = client.post('/authentication/logout/')

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_invalid_logout():
    client = APIClient()
    response = client.post('/authentication/logout/')

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
