from django.db import models
from albums.models import Album
from users.models import User


# Create your models here.

class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    stage_name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    social_link = models.URLField(max_length=300, null=False, blank=True)

    def approved_albums_count(self):
        count = 0
        for album in Album.objects.filter(artist=self):
            count += album.approved
        return count

    def __str__(self):
        return self.stage_name

    class Meta:
        ordering = ["stage_name"]
