from django.urls import path
from .views import inicio, noticias , elenco, sobre, detalhe_noticia

urlpatterns = [
    path('', inicio, name='inicio'),
    path('elenco/', elenco, name='elenco'),
    path('sobre/', sobre, name='sobre'),
    path('noticias/', noticias, name='noticias'),
    path('noticias/<int:noticia_id>/', detalhe_noticia, name='detalhe_noticia'),
]