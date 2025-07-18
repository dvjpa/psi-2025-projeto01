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
            'Fundado em 1976, o Seattle Seahawks rapidamente se tornou uma das franquias mais respeitadas da NFL. Com uma trajetória marcada por grandes conquistas, o time conquistou o Super Bowl XLVIII em 2014, consolidando-se como uma potência no futebol americano. Conhecidos por sua defesa implacável, apelidada de "Legion of Boom", e um ataque dinâmico,'
            ' os Seahawks contam com uma torcida apaixonada que faz do estádio Lumen Field um verdadeiro caldeirão para os adversários. Além das vitórias em campo, o time se destaca pelo forte envolvimento comunitário e por representar com orgulho a cidade de Seattle, inspirando gerações de fãs e atletas.'    
        ),
        'imagem': 'img/seahawks.jpg',
    }
    return render(request, 'index.html', contexto)

def noticias(request):
    noticias = [
        {
            'id': 1,
            'titulo': 'Seattle Seahawks vence o San Francisco 49ers em partida emocionante',
            'data': '10 de julho de 2025',
            'imagem': 'img/seahawks-vs-49ers.jpg',
            'conteudo': '''
        Em um jogo cheio de emoção, o Seattle Seahawks derrotou o San Francisco 49ers por 28 a 24, garantindo uma vitória importante para a temporada.
        A defesa dos Seahawks foi crucial, com várias interceptações no último quarto que garantiram o resultado.
        ''',
        },
        {
            'id': 2,
            'titulo': 'Kenneth Walker III sofre lesão durante treino e preocupa equipe',
            'data': '15 de julho de 2025',
            'imagem': 'img/Kenneth.png',
            'conteudo': '''
        O running back Kenneth Walker III sofreu uma lesão no joelho durante o treino desta terça-feira. Exames preliminares indicam que pode ser necessário um período de recuperação.
        A equipe médica está avaliando o caso, e os torcedores aguardam notícias sobre a volta do atleta.
        ''',
        },
    ]
    return render(request, 'noticias.html', {'noticias': noticias})

def detalhe_noticia(request, noticia_id):
    
    noticias = [
        {
            'id': 1,
            'titulo': 'Seahawks vencem clássico contra 49ers',
            'data': '18 de julho de 2025',
            'conteudo': 'O Seattle Seahawks venceu o rival de divisão em um jogo emocionante...',
        },
        {
            'id': 2,
            'titulo': 'Jogador estrela se machuca em treino',
            'data': '17 de julho de 2025',
            'conteudo': 'Durante o treino da tarde, o jogador sofreu uma torção no joelho...',
        },
    ]
    noticia = next((n for n in noticias if n["id"] == noticia_id), None)
    return render(request, 'noticia_detalhe.html', {'noticia': noticia})



def elenco(request):
    jogadores = [
        {'nome': 'Abraham Lucas', 'posicao': 'Offensive Tackle', 'numero': 70, 'idade': 23, 'foto': 'img/Abraham.png'},
        {'nome': 'Anthony Bradford', 'posicao': 'Guarda', 'numero': 61, 'idade': 24, 'foto': 'img/Anthony.png'},
        {'nome': 'Brady Breeze', 'posicao': 'Safety', 'numero': 26, 'idade': 27, 'foto': 'img/Brady.png'},
        {'nome': 'Charles Cross', 'posicao': 'Offensive Tackle', 'numero': 75, 'idade': 22, 'foto': 'img/Charles.png'},
        {'nome': 'Cooper Kupp', 'posicao': 'Wide Receiver', 'numero': 10, 'idade': 29, 'foto': 'img/Cooper.png'},
        {'nome': 'Drew Lock', 'posicao': 'Quarterback', 'numero': 3, 'idade': 28, 'foto': 'img/Drew.png'},
        {'nome': 'Grey', 'posicao': 'Running Back', 'numero': 33, 'idade': 26, 'foto': 'img/Grey.png'},
        {'nome': 'Jaxon Smith-Njigba', 'posicao': 'Wide Receiver', 'numero': 12, 'idade': 22, 'foto': 'img/Jaxon.png'},
        {'nome': 'Kenneth Walker III', 'posicao': 'Running Back', 'numero': 4, 'idade': 22, 'foto': 'img/Kenneth.png'},
        {'nome': 'Kenny', 'posicao': 'Wide Receiver', 'numero': 13, 'idade': 25, 'foto': 'img/Kenny.png'},
        {'nome': 'Marquez Valdes-Scantling', 'posicao': 'Wide Receiver', 'numero': 11, 'idade': 29, 'foto': 'img/Marquez.png'},
        {'nome': 'Noah Fant', 'posicao': 'Tight End', 'numero': 87, 'idade': 26, 'foto': 'img/Noah.png'},
        {'nome': 'Olusegun Oluwatimi', 'posicao': 'Center', 'numero': 57, 'idade': 24, 'foto': 'img/Olu.png'},
        {'nome': 'Sam', 'posicao': 'Linebacker', 'numero': 51, 'idade': 25, 'foto': 'img/Sam.png'},
    ]
    return render(request, 'elenco.html', {'jogadores': jogadores})

def sobre(request):
    info = {
        'descricao': 'Esté site foi criado como um projeto escolar para a disciplina de PSI, cujo foi instruido que fizessimos ele usando Django, HTML e CSS (os trés cavaleiros do apocalipise) devo ter gastado uma semana e meia para fazer esse trabalho'
        'por ter feito sozinho e ter perdido a aula que explicava direito oque fazer mais pelo menos tive o slide que o professor disponibilizou para os aluno, Na pagina de noticias quando você clica em ver mais ele leva para uma pagina sem nada nela era para aparecer um breve resumo da noticia mais não consegui fazer as paginas mudarem mesmo assim acho que consegui me sair bem melhor do que eu pensava e espero que gostem do meu site.',
        'autores': ['João Paulo Silva',],
    }
    return render(request, 'sobre.html', info)
