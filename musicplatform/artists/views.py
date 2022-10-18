from django.shortcuts import render
from .forms import ArtistFrom


# Create your views here.

def add_artist(request):
    if request.method == "POST":
        artist = ArtistFrom(request.POST)
        if artist.is_valid():
            artist.save()

    context = {'form': ArtistFrom}
    return render(request, 'artists/add_artist.html', context)
