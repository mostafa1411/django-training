from rest_framework import serializers
from .models import Album
from artists.models import Artist


class AlbumSerializer(serializers.ModelSerializer):
    def get_artist(self, album):
        artist = Artist.objects.get(id=album.artist.id)
        return {
            'id': artist.id,
            'stage_name': artist.stage_name,
            'social_link': artist.social_link
        }

    artist = serializers.SerializerMethodField('get_artist')

    class Meta:
        model = Album
        fields = ['id', 'artist', 'name', 'release_datetime', 'cost']
