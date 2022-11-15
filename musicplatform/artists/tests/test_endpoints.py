import pytest
from artists.models import Artist
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_get_list_of_artists():
    artist1 = {
        'stage_name': 'Drake',
    }

    artist2 = {
        'stage_name': 'Ed Sheeran',
    }

    artist3 = {
        'stage_name': '50 Cent',
    }

    client = APIClient()
    client.post('/artists/', artist1)
    client.post('/artists/', artist2)
    client.post('/artists/', artist3)

    response = client.get('/artists/')
    assert response.status_code == status.HTTP_200_OK

    data = response.data
    artists = Artist.objects.all().values()

    assert len(data) == len(artists)

    for i in range(len(data)):
        assert data[i]['id'] == artists[i]['id']
        assert data[i]['stage_name'] == artists[i]['stage_name']
        assert data[i]['social_link'] == artists[i]['social_link']


@pytest.mark.django_db
def test_create_an_artist():
    artist = {
        'stage_name': 'Drake',
    }

    client = APIClient()
    response = client.post('/artists/', artist)
    data = response.data

    assert response.status_code == status.HTTP_201_CREATED
    assert data['stage_name'] == artist['stage_name']


@pytest.mark.django_db
def test_create_artist_with_an_existing_stage_name():
    artist = {
        'stage_name': 'Drake',
    }

    client = APIClient()
    client.post('/artists/', artist)
    response = client.post('/artists/', artist)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
