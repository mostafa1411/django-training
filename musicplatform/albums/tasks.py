from musicplatform import settings
from django.core.mail import send_mail
from celery import shared_task
from .models import Album
from .serializers import AlbumSerializer
from users.models import User
from users.serializers import UserSerializer


@shared_task(bind=True)
def send_congratulation_email(self, album_id, user_id):
    album = Album.objects.get(id=album_id)
    user = User.objects.get(id=user_id)

    album_data = AlbumSerializer(album).data
    user_data = UserSerializer(user).data

    send_mail(
        subject='Congratulations',
        message=f"Hi {user_data['username']},\nCongratulations on creating a new album \'{album_data['name']}'.",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user_data['email']],
        fail_silently=False,
    )

    return None
