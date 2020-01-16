from django.shortcuts import render
from django.http import HttpResponse



def vistaprincipal(request):
	return render(request, 'paginas/vistaprincipal.html')


def login(request):
	return render(request, 'paginas/login.html')

def registrar(request):
	return render(request, 'paginas/registrar.html')


def agendar(request):
	return render(request, 'paginas/agendar.html')

def residentes(request):
	return render(request, 'paginas/residentes.html')

def archivosresidente(request):
	return render(request, 'paginas/archivosresidente.html')

def restablecercontraseña(request):
	return render(request, 'paginas/restablecercontraseña.html')