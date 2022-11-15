import pytest

from users.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from knox.auth import AuthToken


@pytest.fixture
def auth_client():
    def get_client(user=None):
        if user is None:
            user = User.objects.create_user(username="temp", email="temp@gmail.com", password="temp123")

        _, token = AuthToken.objects.create(user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'token {token}')
        return client

    return get_client
