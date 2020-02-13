from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import RegistroForm
from django.contrib.auth.models import User
from banco_proyectos.models import Residente, DatosResidente
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
				if user != True:
					return redirect('/login')
					response.update(
						message = 'correo y/o contraseña incorrecta'
					)
		except Exception as e:
			print('Exception en la vista login => {}'.format(e.args))
		return JsonResponse(response)
	return render(request, 'paginas/login.html')

def logout(request):
	auth_logout(request)
	return render(request, 'paginas/logout.html')

def registrar(request):

	context = {'form': RegistroForm}

	return render(request, 'paginas/registrar.html', context)



#-----------Vista de agendar cita------------
def agendar(request):
	
	if request.method == 'GET':	
		try:
			#Se realiza la consulta a la tabla residente y usuario en la base de datos.
			resident = User.objects.get(username = request.user.username)
			escol = Residente.objects.get(usuario_id = request.user.id)
			#Se guarda el dato en el contexto que se enviara al template agendar
			context = {
			'escol': escol,
			'resident': resident
			}
			#Se guarda en la variable datosr la consulta de la talba datos residentes de la base de datos 
			datosr = DatosResidente.objects.all()
			#Extraemos los datos del residente en variables
			nom = escol.nombre
			apat = resident.first_name
			amat = resident.last_name
			#Se concatenan los datos obtenidos para posterior a ello guaradrlo en la base de datos
			residato = nom +' '+ apat +' '+ amat
			eschol = escol.escuela
			fech = request.GET['fecha']
			DatosResidente.objects.create(
				residente = residato,
				escuela = eschol,
				fecha = fech
			)
		except Exception as e:
			print('Excepción en la vista de agendar => {}'. format(e.args))	
	elif request.method == 'POST':
		try:
			#Se realiza la consulta a la tabla residente y usuario en la base de datos.
			resident = User.objects.get(username = request.user.username)
			escol = Residente.objects.get(usuario_id = request.user.id)
			#Se guarda el dato en el contexto que se enviara al template agendar
			context = {
			'escol': escol,
			'resident': resident
			}
			#Se guarda en la variable datosr la consulta de la talba datos residentes de la base de datos 
			datosr = DatosResidente.objects.all()
			#Extraemos los datos del residente en variables
			nom = escol.nombre
			apat = resident.first_name
			amat = resident.last_name
			#Se concatenan los datos obtenidos para posterior a ello guaradrlo en la base de datos
			residato = nom +' '+ apat +' '+ amat
			eschol = escol.escuela
			fech = request.GET['fecha']
			DatosResidente.objects.create(
				residente = residato,
				escuela = eschol,
				fecha = fech
			)
		except Exception as e:
			print('Excepción en la vista de agendar => {}'. format(e.args))	
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

		datos = Residente(telefono = formula.cleaned_data['telefono'], escuela = formula.cleaned_data['escuela'], nombre = formula.cleaned_data['nombre'] ,usuario = agregar)
		datos.save()
	return render(request, 'paginas/registrar.html')