from django.db import models
from django.utils import timezone
from artists.models import Artist


# Create your models here.

class Album(models.Model):
    name = models.CharField(max_length=50, default=u'New Album')
    creation_time = models.DateTimeField(default=timezone.now)
    release_time = models.DateTimeField(blank=False)
    cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, default='')
