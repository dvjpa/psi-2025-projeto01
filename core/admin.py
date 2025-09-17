from django.contrib import admin
from .models import Jogador, SiteInfo
from .models import PaginaInicial

@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ("nome", "posicao", "numero", "idade")
    search_fields = ("nome", "posicao")
    list_filter = ("posicao",)

@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ("autores",)

admin.site.register(PaginaInicial)