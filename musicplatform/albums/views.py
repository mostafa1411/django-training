from django.shortcuts import render
from .forms import AlbumForm


# Create your views here.

def add_album(request):
    album = AlbumForm(request.POST)
    album.save()

    context = {'form': AlbumForm}
    return render(request, 'albums/add_album.html', context)
