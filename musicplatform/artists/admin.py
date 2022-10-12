from django.contrib import admin
from .models import Artist


class ArtistAdmin(admin.ModelAdmin):
    model = Artist
    list_display = ('stage_name', 'approved_albums_count')


# Register your models here.

admin.site.register(Artist, ArtistAdmin)
