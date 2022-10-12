from django.contrib import admin
from .models import Album

# Register your models here.

admin.site.register(Album)


class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_time', )
