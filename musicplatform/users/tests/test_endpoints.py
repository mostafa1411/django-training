import pytest
from rest_framework import status
from rest_framework.test import APIClient
from users.models import User


@pytest.mark.django_db
def test_get_an_existing_user():
    user = User.objects.create_user(username="mostafa_abdullah",
                                    email="ma@gmail.com",
                                    password="pass123")

    client = APIClient()
    response = client.get(f'/users/{user.id}/')
    data = response.data

    assert response.status_code == status.HTTP_200_OK
    assert data['username'] == 'mostafa_abdullah'
    assert data['email'] == 'ma@gmail.com'
    assert 'bio' in data


@pytest.mark.django_db
def test_get_a_non_existing_user():
    client = APIClient()
    response = client.get('/users/100/')

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_user_full_updates_himself(auth_client):
    user = User.objects.create_user(username="mostafa_abdullah",
                                    email="ma@gmail.com",
                                    password="pass123")

    updated_data = {
        'username': 'mostafa_abdullah2',
        'email': 'new@gmail.com',
        'bio': 'This is my new bio'
    }

    client = auth_client(user)
    response = client.put(f'/users/{user.id}/', updated_data)
    data = response.data

    assert response.status_code == status.HTTP_200_OK
    assert data['id'] == user.id
    assert data['username'] == updated_data['username']
    assert data['email'] == updated_data['email']
    assert data['bio'] == updated_data['bio']


@pytest.mark.django_db
def test_user_partial_updates_himself(auth_client):
    user = User.objects.create_user(username="mostafa_abdullah",
                                    email="ma@gmail.com",
                                    password="pass123")

    updated_bio = {
        'bio': 'This is my bio'
    }

    client = auth_client(user)
    response = client.patch(f'/users/{user.id}/', updated_bio)
    data = response.data

    assert response.status_code == status.HTTP_200_OK
    assert data['id'] == user.id
    assert data['bio'] == updated_bio['bio']


@pytest.mark.django_db
def test_user_full_updates_without_authentication():
    user = User.objects.create_user(username="mostafa_abdullah",
                                    email="ma@gmail.com",
                                    password="pass123")

    updated_data = {
        'username': 'mostafa_abdullah2',
        'email': 'new@gmail.com',
        'bio': 'This is my bio'
    }

    client = APIClient()
    response = client.put(f'/users/{user.id}/', updated_data)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_user_partial_update_without_authentication():
    user = User.objects.create_user(username="mostafa_abdullah",
                                    email="ma@gmail.com",
                                    password="pass123")

    updated_bio = {
        'bio': 'This is my bio'
    }

    client = APIClient()

    response = client.patch(f'/users/{user.id}/', updated_bio)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
