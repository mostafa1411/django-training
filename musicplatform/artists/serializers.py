from rest_framework import serializers
from .models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'stage_name', 'social_link']

    def validate(self, attrs):
        artists = Artist.objects.all()
        for artist in artists:
            if artist.stage_name == attrs.get('stage_name'):
                raise serializers.ValidationError('The stage name is used by another artist')

        return attrs
