from django.urls import path
from . import views

urlpatterns = [
    path('', views.AlbumView.as_view(), name='album'),
]
