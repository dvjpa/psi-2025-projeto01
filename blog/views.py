from django.shortcuts import render
from .models import Noticia

def noticias(request):
    posts = Noticia.objects.order_by('-data_publicacao')
    return render(request, 'core/noticias.html', {'noticias': posts})

