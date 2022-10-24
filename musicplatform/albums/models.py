from django.core.exceptions import ValidationError
from django.db import models
from model_utils.models import TimeStampedModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.


class Album(TimeStampedModel):
    name = models.CharField(max_length=50, default=u'New Album')
    release_time = models.DateTimeField(blank=False)
    cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    artist = models.ForeignKey('artists.Artist', on_delete=models.CASCADE, default='')
    approved = models.BooleanField(default=False, help_text='Approve the album if its name is not explicit')

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=50, blank=True, default='')
    image = models.ImageField(upload_to='images/%y/%m/%d', null=False, blank=False)
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(100, 50)],
                                     format='JPEG',)
    audio = models.FileField(upload_to='audio/%y/%m/%d', null=False, blank=False)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name == '':
            self.name = self.album.name

        return super(Song, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.album.song_set.count() == 1:
            raise ValidationError("This song cannot be deleted as it's album has only 1 song")
        else:
            return super(Song, self).delete(*args, **kwargs)