from django.contrib import admin
from .models import Categoria, Artigo, MensagemContato, Comentario


# Register your models here.

admin.site.register(Categoria)


@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'data_publicacao')

    search_fields = ('titulo', 'conteudo')

    list_filter = ('categoria', 'data_publicacao')


admin.site.register(MensagemContato)


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'artigo', 'data_criacao')

    search_fields = ('nome', 'texto')

    list_filter = ('data_criacao',)
