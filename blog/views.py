from django.shortcuts import render, get_object_or_404
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

    categorias = Categoria.objects.all()

    contexto = {
        'lista_categorias': categorias,
    }

    return render(request, "blog/sobre.html", contexto)


def categoria(request, categoria_id):

    categoria = get_object_or_404(Categoria, id=categoria_id)
    artigos = Artigo.objects.filter(categoria_id=categoria_id)
    categorias = Categoria.objects.all()

    contexto = {
        'categoria': categoria,
        'lista_artigos': artigos,
        'lista_categorias': categorias,
    }

    return render(request, "blog/categoria.html", contexto)


def artigo_detalhe(request, id):
    categorias = Categoria.objects.all()

    noticia = get_object_or_404(Artigo, id=id)

    contexto = {
        'lista_categorias': categorias,
        'artigo': noticia,
    }

    return render(request, 'blog/artigo_detalhe.html', contexto)