from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.UserViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update'
    }), name='user')
]
