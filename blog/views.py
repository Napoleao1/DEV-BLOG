from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    
    return render(request, "blog/index.html")    
    return HttpResponse(mensagem) 


def sobre_nos(request):
    
    return render(request, "blog/sobre.html")
    return HttpResponse(mensagem)