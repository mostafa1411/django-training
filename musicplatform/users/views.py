from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


# Create your views here.


class UserView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def get(self, request, pk):
        users = list(User.objects.filter(id=pk))

        if not users:
            return Response("User is not found", status=status.HTTP_404_NOT_FOUND)

        user = users[0]

        return Response({
            "user": {
                "id": user.pk,
                "username": user.username,
                "email": user.email,
                "bio": user.bio
            }
        }, status=status.HTTP_200_OK)
