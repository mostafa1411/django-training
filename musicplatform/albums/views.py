from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions, generics, viewsets
from .models import Album
from .serializers import AlbumSerializer
from django_filters import rest_framework as filters

# Create your views here.


class AlbumFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Album
        fields = {
            'name': ['icontains'],
            'cost': ['lte', 'gte']
        }


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.filter(approved=True)
    serializer_class = AlbumSerializer
    filterset_class = AlbumFilter

    @permission_classes([permissions.AllowAny])
    def get(self, request):
        albums = Album.objects.filter(approved=True)
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @permission_classes([permissions.IsAuthenticated])
    def create(self, request):
        if not hasattr(request.user, 'artist'):
            return Response('This user is not an artist', status=status.HTTP_403_FORBIDDEN)

        serializer = AlbumSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(artist=request.user.artist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
