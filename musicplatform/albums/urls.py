from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.add_album, name='add_album')
]
