from django.contrib import admin
from .models import Noticia

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao')
    ordering = ('-data_publicacao',)
    fields = ('titulo', 'conteudo', 'imagem', 'data_publicacao')
    readonly_fields = ('data_publicacao',)