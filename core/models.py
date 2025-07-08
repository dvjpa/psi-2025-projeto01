from django.db import models

class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    posicao = models.CharField(max_length=50)
    nascimento = models.DateField()
    foto = models.ImageField(upload_to='fotos_jogadores/')

    def __str__(self):
        return self.nome