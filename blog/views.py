from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Artigo, Categoria
from .forms import ContatoForm, ComentarioForm
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator

from .serializer import ArtigoSerializer, CategoriaSerializer


def home(request):

    noticias = Artigo.objects.all().order_by('-id')
    categorias = Categoria.objects.all()

    # 1. Captura o que o usuário digitou na busca
    busca = request.GET.get('q')

    # 2. Filtra o banco se houver termo de busca
    if busca:
        noticias = noticias.filter(titulo__icontains=busca)

    paginator = Paginator(noticias, 5)
    numero_da_pagina = request.GET.get('page')
    page_obj = paginator.get_page(numero_da_pagina)

    contexto = {
        'lista_artigos': page_obj,
        'lista_categorias': categorias,
        'termo': busca,
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

    if request.method == "POST":
        formulario = ComentarioForm(request.POST)

        if formulario.is_valid():
            comentario = formulario.save(commit=False)
            comentario.artigo = noticia
            comentario.save()
            return redirect('artigo_detalhe', id=noticia.id)

    else:
        formulario = ComentarioForm()

    contexto = {
        'lista_categorias': categorias,
        'artigo': noticia,
        'comentarios': noticia.comentarios.all(),
        'form_comentario': formulario,
    }

    return render(request, 'blog/artigo_detalhe.html', contexto)


def buscar(request):
    categorias = Categoria.objects.all()

    termo = request.GET.get('q', '').strip()

    if termo:
        artigos = Artigo.objects.filter(
            Q(titulo__icontains=termo) | Q(conteudo__icontains=termo)
        )
    else:
        artigos = Artigo.objects.none()

    contexto = {
        'lista_categorias': categorias,
        'lista_artigos': artigos,
        'termo': termo,
    }

    return render(request, 'blog/busca.html', contexto)


def fale_conosco(request):
    categorias = Categoria.objects.all()

    if request.method == "POST":
        formulario = ContatoForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('home')

    else:
        formulario = ContatoForm()

    contexto = {
        'lista_categorias': categorias,
        'form': formulario,
    }

    return render(request, 'blog/contato.html', contexto)


@api_view(['GET'])
def api_listar_artigos(request):
    artigo = Artigo.objects.all()

    serializer = ArtigoSerializer(artigo, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def api_listar_categorias(request):
    categoria = Categoria.objects.all()

    serializer = CategoriaSerializer(categoria, many=True)

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_criar_artigo(request):
    
    serializer = ArtigoSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    
    return Response(serializer.errors, status=400)