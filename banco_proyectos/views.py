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


def bienvenido(request):
	return render(request, 'paginas/bienvenido.html')


def vistaprincipal(request):
	return render(request, 'paginas/vistaprincipal.html')

def login(request):

	response = {
	'message': '',
	'success': False,
	}

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		try:
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					auth_login(request, user)
					if request.user.is_authenticated:
						return redirect('/vistaprincipal')
						response.update(
							message = 'Inicio de sesion correcta',
							success = True
						)
				else:
					response.update(
						message = 'Usuario inactivo'
					)
			else:
				response.update(
					message = 'correo y/o contraseña incorrecta'
				)
		except Exception as e:
			print('Exception en la vista login => {}'.format(e.args))
		return JsonResponse(response)
	return render(request, 'paginas/login.html')

def logout(request):
	auth_logout(request)
	return render(request, 'paginas/bienvenido.html')

def registrar(request):

	context = {'form': RegistroForm}

	return render(request, 'paginas/registrar.html', context)



#-----------Vista de agendar cita------------
def agendar(request):
	#Se realiza la consulta a la tabla residente en la base de datos.
	if request.method == 'POST':	
		resident = User.objects.get(username = request.user.username)
		escol = residente.objects.get(usuario_id = request.user.id)
		#Se guarda el dato en el contexto que se enviara al template agendar
		context = {
		'escol': escol,
		'resident': resident
		}
	else:
		if request.method == 'GET':
			resident = User.objects.get(username = request.user.username)
			escol = residente.objects.get(usuario_id = request.user.id)
			#Se guarda el dato en el contexto que se enviara al template agendar
			context = {
			'escol': escol,
			'resident': resident
			}
	return render(request, 'paginas/agendar.html', context)




def residentes(request):
	return render(request, 'paginas/residentes.html')

def archivosr(request):
	return render(request, 'paginas/archivosr.html')


#-----------Vista de restablecer contraseña------------
def restablecercontraseña(request):
	


	return render(request, 'paginas/restablecercontraseña.html')

	
#-----------Vista de ver proyectos------------
def verproyectos(request):
	return render(request, 'paginas/verproyectos.html')

#-----------Vista de agregar usuario------------
def agregar_usuario(request):
	formula = RegistroForm(request.POST)

	if formula.is_valid():

		agregar = User(username = formula.cleaned_data['correo'], first_name = formula.cleaned_data['apaterno'], last_name = formula.cleaned_data['amaterno'])
		agregar.set_password(formula.cleaned_data['password'])
		agregar.save()

		datos = residente(telefono = formula.cleaned_data['telefono'], escuela = formula.cleaned_data['escuela'], nombre = formula.cleaned_data['nombre'] ,usuario = agregar)
		datos.save()
	return render(request, 'paginas/registrar.html')