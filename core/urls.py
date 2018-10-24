from django.urls import path
from .views import index, busca, cidade

urlpatterns = [
    path('index/', index, name='index'),
    path('busca/', busca, name='busca'),
    path('cidade/', cidade, name='cidade'),
]