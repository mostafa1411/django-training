from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.ArtistCreateView.as_view(), name='add_artist'),
]
