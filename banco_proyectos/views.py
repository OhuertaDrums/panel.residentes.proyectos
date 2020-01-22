from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import RegistroForm
from django.contrib.auth.models import User
from banco_proyectos.models import residente
from pdb import set_trace
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

@login_required(login_url='/login/')
def bienvenido(request):
	return render(request, 'paginas/bienvenido.html')

@login_required(login_url='/login/')
def vistaprincipal(request):
	return render(request, 'paginas/vistaprincipal.html')

@login_required(login_url='/login/')
def login(request):

	response = {
		'message': '',
		'success': False,
		'path': ''
	}
	 # Añadimos los datos recibidos al formulario
	if request.user.is_authenticated:
		
		if request.method == 'POST':
		# Recuperamos las credenciales validadas
			username = request.POST.get('username')
			password = request.POST.get('password')
			try:
				# Verificamos las credenciales del usuario
				user = authenticate(username=username, password=password)
				if user is not None:
					if user.is_active:
						auth_login(request, user)
						response.update(
							message = 'Inicio de sesion correcto',
							success = True,
							path = '/vistaprincipal/'
						)
						return redirect('/vistaprincipal')
					else:
						response.update(
							message = 'Usuario inactivo'
						)
				else:
					response.update(
						message = 'Usuario y/o correo incorrecto'
					)
			except Exception as e:
				print('Excepcion en la vista login => {}'.format(e.args))
			#return JsonResponse(response)
	return render(request, 'paginas/login.html')

def registrar(request):

	context = {'form': RegistroForm}

	return render(request, 'paginas/registrar.html', context)


def agendar(request):
	return render(request, 'paginas/agendar.html')

def residentes(request):
	return render(request, 'paginas/residentes.html')

def archivosr(request):
	return render(request, 'paginas/archivosr.html')

def restablecercontraseña(request):
	return render(request, 'paginas/restablecercontraseña.html')

def verproyectos(request):
	return render(request, 'paginas/verproyectos.html')


def agregar_usuario(request):
	formula = RegistroForm(request.POST)

	if formula.is_valid():

		agregar = User(username = formula.cleaned_data['nombre'], 
			email = formula.cleaned_data['correo'])
		agregar.set_password(formula.cleaned_data['password'])
		agregar.save()

		datos = residente(telefono = formula.cleaned_data['telefono'], escuela = formula.cleaned_data['escuela'])
		datos.save()
	return render(request, 'paginas/registrar.html')