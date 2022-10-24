from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from .forms import ArtistForm
from .models import Artist
from django.views import View

# Create your views here.


class IndexView(View):
    def get(self, request):
        context = {'artists': Artist.objects.all()}
        return render(request, 'artists/index.html', context)


class ArtistCreateView(CreateView):
    template_name = 'artists/add_artist.html'

    @method_decorator(login_required)
    def get(self, request):
        context = {'form': ArtistForm}
        return render(request, self.template_name, context)

    def post(self, request):
        artist = ArtistForm(request.POST)
        if artist.is_valid():
            artist.save()

        context = {'form': ArtistForm}
        return render(request, self.template_name, context)
