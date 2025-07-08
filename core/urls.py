from django.urls import path
from .views import inicio, elenco, sobre

urlpatterns = [
    path('', inicio, name='inicio'),
    path('elenco/', elenco, name='elenco'),
    path('sobre/', sobre, name='sobre'),
]