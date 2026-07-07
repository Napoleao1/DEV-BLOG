from django.urls import path
from . import views


urlpatterns = [


    path('', views.home, name='home'),
    path('sobre/', views.sobre_nos, name='sobre_nos'),
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),
    path('artigo/<int:id>/', views.artigo_detalhe, name='artigo_detalhe'),
    path('contato/', views.fale_conosco, name='fale_conosco'),
    path('api/artigos/', views.api_listar_artigos, name='api_artigos'),
    path('api/categorias/', views.api_listar_categorias, name='api_categorias')
]
