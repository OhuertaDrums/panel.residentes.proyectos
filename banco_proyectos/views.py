from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(" Bienvenido al Banco de Proyectos FINKOK")

def base(request):

   return render (request, 'index.html')


def pruebas(request):
	return render(request, 'paginas/pruebas.html')


def login(request):
	return render(request, 'paginas/login.html')

def registrar(request):
	return render(request, 'paginas/registrar.html')

def calendario(request):
	return render(request, 'paginas/calendario.html')

def test(request):
	return render(request, 'paginas/test.html')