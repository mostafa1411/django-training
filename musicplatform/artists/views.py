from django.shortcuts import render
from .forms import ArtistForm
from .models import Artist, Album
from django.views import View

# Create your views here.


class IndexView(View):
    def get(self, request):
        context = {'artists': Artist.objects.all()}
        return render(request, 'artists/index.html', context)


class ArtistCreateView(View):
    template_name = 'artists/add_artist.html'

    def get(self, request):
        context = {'form': ArtistForm}
        return render(request, self.template_name, context)

    def post(self, request):
        artist = ArtistForm(request.POST)
        if artist.is_valid():
            artist.save()

        context = {'form': ArtistForm}
        return render(request, self.template_name, context)
