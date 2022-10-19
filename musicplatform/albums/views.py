from django.shortcuts import render
from .forms import AlbumForm


# Create your views here.

def add_album(request):
    if request.method == "POST":
        album = AlbumForm(request.POST)
        if album.is_valid():
            album.save()

    context = {'form': AlbumForm}
    return render(request, 'albums/add_album.html', context)
