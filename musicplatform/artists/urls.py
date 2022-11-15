from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArtistView.as_view(), name='artist'),
]
