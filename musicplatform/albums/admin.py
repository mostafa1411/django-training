from django.contrib import admin
from .models import Album


class AlbumAdmin(admin.ModelAdmin):
    model = Album
    readonly_fields = ('creation_time', )


# Register your models here.

admin.site.register(Album, AlbumAdmin)
