from django.shortcuts import render
from .models import Artigo, Categoria


def home(request):

    noticias = Artigo.objects.all()
    categorias = Categoria.objects.all()
    contexto = {
        'lista_artigos': noticias,
        'lista_categorias': categorias,
    }

    return render(request, "blog/index.html", contexto)


def sobre_nos(request):
    return render(request, "blog/sobre.html")


def categoria(request, categoria_id):

    categoria = Categoria.objects.get(id=categoria_id)
    artigos = Artigo.objects.filter(categoria_id=categoria_id)
    categorias = Categoria.objects.all()

    contexto = {
        'categoria': categoria,
        'lista_artigos': artigos,
        'lista_categorias': categorias,
    }

    return render(request, "blog/categoria.html", contexto)
