import pytest
import pytz

from datetime import datetime
from decimal import Decimal
from albums.models import Album
from artists.models import Artist
from rest_framework import status
from rest_framework.test import APIClient
from users.models import User


@pytest.mark.django_db
def test_get_albums_list():
    user1 = User.objects.create_user(username='user1',
                                     email='user1@gmail.com',
                                     password='user123')
    user2 = User.objects.create_user(username='user2',
                                     email='user2@gmail.com',
                                     password='user456')

    artist1 = Artist.objects.create(user=user1, stage_name='artist1')
    artist2 = Artist.objects.create(user=user2, stage_name='artist2')

    album1 = Album.objects.create(artist=artist1,
                                  name='album1',
                                  release_datetime='2022-01-01',
                                  cost=100,
                                  approved=True)
    album2 = Album.objects.create(artist=artist2,
                                  name='album2',
                                  release_datetime='2022-02-02',
                                  cost=200,
                                  approved=False)
    album3 = Album.objects.create(artist=artist1,
                                  name='album3',
                                  release_datetime='2022-03-03',
                                  cost=300,
                                  approved=False)
    album4 = Album.objects.create(artist=artist2,
                                  name='album4',
                                  release_datetime='2022-04-04',
                                  cost=400,
                                  approved=True)

    approved_albums = [album1, album4]

    client = APIClient()
    response = client.get('/albums/')
    data = response.data['results']

    assert response.status_code == status.HTTP_200_OK
    assert len(data) == len(approved_albums)

    for i in range(len(data)):
        assert approved_albums[i].approved
        assert data[i]['id'] == approved_albums[i].id
        assert data[i]['name'] == approved_albums[i].name
        assert data[i]['release_datetime'][:10] == approved_albums[i].release_datetime
        assert float(data[i]['cost']) == float(approved_albums[i].cost)
        assert data[i]['artist']['id'] == approved_albums[i].artist.id
        assert data[i]['artist']['stage_name'] == approved_albums[i].artist.stage_name
        assert data[i]['artist']['social_link'] == approved_albums[i].artist.social_link


@pytest.mark.django_db
def test_create_an_album(auth_client):
    user = User.objects.create_user(username='user',
                                    email='user@gmail.com',
                                    password='user123')
    artist = Artist.objects.create(user=user, stage_name='artist')

    album = {
        'name': 'album',
        'release_datetime': '2011-01-01',
        'cost': 500
    }

    client = auth_client(user)
    response = client.post('/albums/', album)
    data = response.data

    assert response.status_code == status.HTTP_201_CREATED
    assert data['name'] == album['name']
    assert data['release_datetime'][:10] == album['release_datetime']
    assert float(data['cost']) == float(album['cost'])
    assert data['artist']['id'] == artist.id
    assert data['artist']['stage_name'] == artist.stage_name
    assert data['artist']['social_link'] == artist.social_link


@pytest.mark.django_db
def test_create_an_album_with_invalid_cost(auth_client):
    user = User.objects.create_user(username='user',
                                    email='user@gmail.com',
                                    password='user123')
    artist = Artist.objects.create(user=user, stage_name='artist')

    album = {
        'name': 'album',
        'release_datetime': '2011-01-01',
        'cost': 'value'
    }

    client = auth_client(user)
    response = client.post('/albums/', album)

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_create_an_album_by_an_unauthenticated_user():
    user = User.objects.create_user(username='user',
                                    email='user@gmail.com',
                                    password='user123')
    artist = Artist.objects.create(user=user, stage_name='artist')

    album = {
        'name': 'album',
        'release_datetime': '2011-01-01',
        'cost': 'value'
    }

    client = APIClient()
    response = client.post('/albums/', album)

    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_create_an_album_by_an_authenticated_user_but_not_an_artist(auth_client):
    user = User.objects.create_user(username='user',
                                    email='user@gmail.com',
                                    password='user123')
    artist = Artist.objects.create(user=user, stage_name='artist')

    album = {
        'name': 'album',
        'release_datetime': '2011-01-01',
        'cost': 'value'
    }

    client = auth_client()
    response = client.post('/albums/', album)

    assert response.status_code == status.HTTP_403_FORBIDDEN
