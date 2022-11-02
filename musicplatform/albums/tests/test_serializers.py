import pytest
from albums.serializers import AlbumSerializer
from albums.models import Album
from artists.models import Artist
from users.models import User


@pytest.mark.django_db
def test_serializer():
    user = User.objects.create_user(username='user',
                                    email='user@gmail.com',
                                    password='user123')
    artist = Artist.objects.create(user=user, stage_name='artist')
    album = Album.objects.create(artist=artist,
                                 name='album',
                                 release_datetime='2022-01-01',
                                 cost=500)

    serializer = AlbumSerializer(album)
    data = serializer.data

    assert data['id'] == album.id
    assert data['name'] == album.name
    assert float(data['cost']) == float(album.cost)
    assert data['release_datetime'] == album.release_datetime
    assert data['artist']['id'] == artist.id
    assert data['artist']['stage_name'] == artist.stage_name
    assert data['artist']['social_link'] == artist.social_link


@pytest.mark.django_db
def test_deserializer():
    serializer = AlbumSerializer(data={
        'name': "test_album",
        'release_datetime': '2022-01-01',
        'cost': 500
    })

    serializer.is_valid(raise_exception=False)
    assert not serializer.errors
    assert serializer.validated_data['name'] == 'test_album'
    assert float(serializer.validated_data['cost']) == 500.00
