from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')

def index(request):
    return render(request, 'main/index.html')

def arquiteturaeurbanismo(request):
    return render(request, 'main/arquiteturaeurbanismo.html')

def engenhariacivil(request):
    return render(request, 'main/engenhariacivil.html')

def cienciacomputacao(request):
    return render(request, 'main/cienciacomputacao.html')
