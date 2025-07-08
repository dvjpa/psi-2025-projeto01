from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá, mundo! Essa é a homepage.")

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

from django.shortcuts import render
def inicio(request):
    contexto = {
        'titulo': 'Seattle Seahawks',
        'descricao': 'Site oficial do Seattle Seahawks - NFL',
        'historia': (
            'Fundado em 1976, o Seattle Seahawks é um dos times mais fortes da NFL, '
            'com um Super Bowl vencido e uma torcida apaixonada.'
        ),
        'imagem': 'img/seahawks.jpg',
    }
    return render(request, 'index.html', contexto)

def elenco(request):
    jogadores = [
        {'nome': 'Russell Wilson', 'idade': 32, 'posicao': 'Quarterback', 'nascimento': 'Cincinnati, OH', 'foto': 'wilson.jpg'},
        {'nome': 'Tyler Lockett', 'idade': 29, 'posicao': 'Wide Receiver', 'nascimento': 'Tulsa, OK', 'foto': 'lockett.jpg'},
        {'nome': 'DK Metcalf', 'idade': 24, 'posicao': 'Wide Receiver', 'nascimento': 'Oxford, MS', 'foto': 'metcalf.jpg'},
        {'nome': 'Bobby Wagner', 'idade': 30, 'posicao': 'Linebacker', 'nascimento': 'Los Angeles, CA', 'foto': 'wagner.jpg'},
        {'nome': 'Jadeveon Clowney', 'idade': 28, 'posicao': 'Defensive End', 'nascimento': 'Rock Hill, SC', 'foto': 'clowney.jpg'},
        {'nome': 'Chris Carson', 'idade': 27, 'posicao': 'Running Back', 'nascimento': 'Fort Lauderdale, FL', 'foto': 'carson.jpg'},
        {'nome': 'Quandre Diggs', 'idade': 29, 'posicao': 'Safety', 'nascimento': 'Detroit, MI', 'foto': 'diggs.jpg'},
        {'nome': 'Jam Seattle', 'idade': 25, 'posicao': 'Cornerback', 'nascimento': 'Seattle, WA', 'foto': 'jam.jpg'},
        {'nome': 'Geno Smith', 'idade': 31, 'posicao': 'Quarterback', 'nascimento': 'Miami, FL', 'foto': 'smith.jpg'},
        {'nome': 'Carlos Dunlap', 'idade': 33, 'posicao': 'Defensive End', 'nascimento': 'Chattanooga, TN', 'foto': 'dunlap.jpg'},
        {'nome': 'Rashaad Penny', 'idade': 26, 'posicao': 'Running Back', 'nascimento': 'Norwalk, CA', 'foto': 'penny.jpg'},
    ]
    return render(request, 'core/elenco.html', {'jogadores': jogadores})

def sobre(request):
    info = {
        'descricao': 'Site criado como projeto escolar para divulgar o Seattle Seahawks.',
        'autores': ['João Paulo Silva',],
    }
    return render(request, 'sobre.html', info)

from django.shortcuts import render
from .models import Jogador

def elenco(request):
    jogadores = Jogador.objects.all()  # pega todos os jogadores
    return render(request, 'core/elenco.html', {'jogadores': jogadores})