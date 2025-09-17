from django.db import models


class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    posicao = models.CharField(max_length=50)
    numero = models.IntegerField()
    idade = models.IntegerField()
    foto = models.ImageField(upload_to='jogadores/')

    def __str__(self):
        return f"{self.numero} - {self.nome}"


class SiteInfo(models.Model):
    descricao = models.TextField()
    autores = models.CharField(max_length=255)

    def __str__(self):
        return "Informações do site"
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField()
    image = models.ImageField(upload_to='noticias/')

class PaginaInicial(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    historia = models.TextField()
    imagem = models.ImageField(upload_to='index/')

    def __str__(self):
        return self.titulo