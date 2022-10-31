from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Artist
from .serializers import ArtistSerializer

# Create your views here.


class ArtistView(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArtistSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
