from django.shortcuts import render
from .models import Album
from .forms import AlbumForm
from django.views import View
from django.views.generic.edit import CreateView


# Create your views here.

class AlbumCreateView(CreateView):
    template_name = 'albums/add_album.html'

    def get(self, request):
        context = {'form': AlbumForm}
        return render(request, self.template_name, context)

    def post(self, request):
        album = AlbumForm(request.POST)
        if album.is_valid():
            album.save()

        context = {'form': AlbumForm}
        return render(request, self.template_name, context)
