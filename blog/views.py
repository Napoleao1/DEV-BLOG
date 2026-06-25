from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    
    mensagem = "<h1> Bem vindo ao devblog </h1> <p> Em breve, artigos aqui. </p>"
    
    return HttpResponse(mensagem) 


def sobre_nos(request):
    
    mensagem = "<h3>Sobre o Devblog </h3>"
    
    return HttpResponse(mensagem)