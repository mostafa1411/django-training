from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserSerializer


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = {permissions.IsAuthenticatedOrReadOnly}
    queryset = User.objects.all()
