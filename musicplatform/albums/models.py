from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.


class Album(TimeStampedModel):
    name = models.CharField(max_length=50, default=u'New Album')
    release_time = models.DateTimeField(blank=False)
    cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    artist = models.ForeignKey('artists.Artist', on_delete=models.CASCADE, default='')
    approved = models.BooleanField(default=False, help_text='Approve the album if its name is not explicit')
