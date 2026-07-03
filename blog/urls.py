from django.urls import path
from . import views


urlpatterns = [
    
    
    path('', views.home, name='home'),
    path('sobre/', views.sobre_nos, name='sobre_nos'),
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),
    path('artigo/<int:id>/', views.artigo_detalhe, name='artigo_detalhe'),
]