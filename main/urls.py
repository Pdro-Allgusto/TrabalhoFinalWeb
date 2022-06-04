from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('cienciacomputacao/', cienciacomputacao, name='cienciacomputacao'),
    path('engenhariacivil/', engenhariacivil, name='engenhariacivil'),
    path('arquiteturaeurbanismo/', arquiteturaeurbanismo, name='arquiteturaeurbanismo'),
]
