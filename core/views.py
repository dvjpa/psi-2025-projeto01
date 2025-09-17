from django.shortcuts import render
from blog.models import Noticia
from core.models import Jogador, SiteInfo
from .models import PaginaInicial

def inicio(request):
    pagina = PaginaInicial.objects.first()
    contexto = {
        'titulo': pagina.titulo if pagina else 'Seattle Seahawks',
        'descricao': pagina.descricao if pagina else 'Site oficial do Seattle Seahawks - NFL',
        'historia': pagina.historia if pagina else '',
        'imagem': pagina.imagem.url if pagina and pagina.imagem else 'img/seahawks.jpg',
    }
    return render(request, 'index.html', contexto)

def noticias(request):
    posts = Noticia.objects.order_by('-data_publicacao')
    return render(request, 'noticias.html', {'noticias': posts})

def elenco(request):
    jogadores = Jogador.objects.all()
    return render(request, 'elenco.html', {'jogadores': jogadores})

def sobre(request):
    info = SiteInfo.objects.first()
    autores = info.autores.split(',') if info else []
    return render(request, 'sobre.html', {
        'descricao': info.descricao if info else '',
        'autores': [autor.strip() for autor in autores],
    })