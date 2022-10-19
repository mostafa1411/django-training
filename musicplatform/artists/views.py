from django.shortcuts import render
from .forms import ArtistFrom
from .models import Artist, Album


# Create your views here.

def index(request):
    context = {'artists': Artist.objects.all()}
    return render(request, 'artists/index.html', context)


def add_artist(request):
    if request.method == "POST":
        artist = ArtistFrom(request.POST)
        if artist.is_valid():
            artist.save()

    context = {'form': ArtistFrom}
    return render(request, 'artists/add_artist.html', context)
