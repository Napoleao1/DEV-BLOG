from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    
    return render(request, "blog/index.html")    
    return HttpResponse(mensagem) 


def sobre_nos(request):
    
    mensagem = "<h3>Sobre o Devblog </h3>"
    return HttpResponse(mensagem)