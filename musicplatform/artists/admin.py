from django.contrib import admin
from .models import Artist, Album


class AlbumInline(admin.StackedInline):
    model = Album
    extra = 0


class ArtistAdmin(admin.ModelAdmin):
    model = Artist
    list_display = ('stage_name', 'approved_albums_count')
    inlines = [AlbumInline]


# Register your models here.

admin.site.register(Artist, ArtistAdmin)
