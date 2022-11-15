from musicplatform import settings
from django.core.mail import send_mail
from celery import shared_task
from .models import Album
from .serializers import AlbumSerializer
from users.models import User
from users.serializers import UserSerializer
from artists.models import Artist
from datetime import datetime, timezone


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


@shared_task(bind=True)
def send_email_for_inactivity_for_month(self):
    artists = Artist.objects.all()
    for artist in artists:
        if artist.album_set.all().count() == 0:
            continue

        differance = datetime.now(timezone.utc) - artist.album_set.all().latest('release_datetime').release_datetime
        if differance.days > 30:
            # print(f"Should send mail to {artist.user.email}")
            send_mail(
                subject='Attention',
                message=f'Hi {artist.stage_name}\nYou have not created an album in the past 30 days, so, '
                        f'we send you this email letting you know that your inactivity is causing your popularity '
                        f'on our platform to decrease.',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[artist.user.email],
                fail_silently=False
            )

    return None
