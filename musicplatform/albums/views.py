from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Album
from .serializers import AlbumSerializer

# Create your views here.


class AlbumView(APIView):
    @permission_classes([permissions.AllowAny])
    def get(self, request):
        albums = Album.objects.filter(approved=True)
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @permission_classes([permissions.IsAuthenticated])
    def post(self, request):
        if not hasattr(request.user, 'artist'):
            return Response('This user is not an artist', status=status.HTTP_403_FORBIDDEN)

        serializer = AlbumSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(artist=request.user.artist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
