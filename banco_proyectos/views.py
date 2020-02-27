from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import RegistroForm
from .forms import Imagenes
from django.contrib.auth.models import User
from banco_proyectos.models import Residente, DatosResidente, Archivos_residentes, Administradores
from pdb import set_trace
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from pdb import set_trace
from django.template.loader import render_to_string

#-----------Vista principal donde el usuario interactua con el sistema------------
def bienvenido(request):
	return render(request, 'paginas/bienvenido.html')

#-----------Vista principal donde el residente **1er ETAPA**------------
def vistaprincipal(request):
	return render(request, 'paginas/vistaprincipal.html')


#-----------Vista de inicio de sesion------------
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
						#comentario / Redirecciona a las vistas principales admins, residentes no borrar,

	    				#return redirect('/vistaprincipal')
	    				#return redirect('/residentes')
	    				return redirect('/panel-administrativo')
	    				
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


#-----------Vista Sesion cerrada------------
def logout(request):
	auth_logout(request)
	return render(request, 'paginas/logout.html')

#-----------Vista donde se regitra el residente------------
def registrar(request):

	context = {'form': RegistroForm}

	return render(request, 'paginas/registrar.html', context)



#-----------Vista donde agendara cita el residente------------
def agendar(request):
	
	if request.method == 'POST':	
		try:
			#Se realiza la consulta a la tabla residente y usuario en la base de datos.
			resident = User.objects.get(username = request.user.username)
			escol = Residente.objects.get(usuario_id = request.user.id)
			username = User(request.user.id)
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
			fech = request.POST['fecha']
			DatosResidente.objects.create(
				residente = residato,
				escuela = eschol,
				fecha = fech,
				usuario = username
			)
		except Exception as e:
			print('Excepción en la vista de agendar => {}'. format(e.args))	
	elif request.method == 'GET':
		return render(request, 'paginas/agendar.html')
	return render(request, 'paginas/agendar.html', context)



#-----------Vista principal del residente **2da ETAPA**------------
def residentes(request):
	return render(request, 'paginas/residentes.html')


#-----------Vista donde subira archivos el residente------------
def archivosr(request):
	if request.method == 'POST':
		try:
			acta = request.FILES.get('acta')
			curp = request.FILES.get('curp')
			ine = request.FILES.get('ine')
			domicilio = request.FILES.get('com_domicilio')
			c_estudios = request.FILES.get('comp_estudios')
			c_presentacion = request.FILES.get('carta_present')
			cer_medico = request.FILES.get('cert_medico')
			username = User(request.user.id)
		
			Archivos_residentes.objects.create(
					acta_nacimiento=acta,
					curp=curp,
					Ine=ine,
					domicilio=domicilio,
					comprobante_estudio=c_estudios,
					carta_presentación=c_presentacion,
					certificado_medico=cer_medico,
					user=username
			)
				
		except Exception as e:
			print('Excepción en la vista archivosr => {}'. format(e.args))
	elif request.method == 'GET':
		return render(request, 'paginas/archivosr.html')
	return render(request, 'paginas/archivosr.html')


#-----------Vista de restablecer contraseña------------
def restablecercontraseña(request):
	

	return render(request, 'paginas/restablecercontraseña.html')

	
#-----------Vista donde vera los proyectos el residente------------
def verproyectos(request):
	
	return render(request, 'paginas/verproyectos.html')

#-----------Vista donde se agregaran los usuarios------------
def agregar_usuario(request):
	formula = RegistroForm(request.POST)

	if formula.is_valid():

		agregar = User(username = formula.cleaned_data['correo'], first_name = formula.cleaned_data['apaterno'], last_name = formula.cleaned_data['amaterno'])
		agregar.set_password(formula.cleaned_data['password'])
		agregar.save()

		datos = Residente(telefono = formula.cleaned_data['telefono'], escuela = formula.cleaned_data['escuela'], nombre = formula.cleaned_data['nombre'] ,usuario = agregar)
		datos.save()
	return render(request, 'paginas/registrar.html')




#-----------Vista general de los administradores------------
def panel_administradores(request):
	return render(request, 'paginas/panel_admins.html')


#-----------Vista donde veran los admins las citas de los residentes------------
def ver_citas(request, *args, **kwargs):
	contexto = {}
	try:
		if request.method == 'POST' and request.is_ajax():
			#En cada petion  ajax a la vista se incluye la accion a realizar con la variable opccion
			opccion = request.POST.get('opccion')
			#evaluas que quieres hacer con la variable option
			if opccion == "agendar_cita":
        # Aqui puedes replicar el proceso en la peticiones ajax que hagas y solo los datos los retornas en el json responso con
        # la misma estrucutra del contexto
				pass

			elif opccion == "datable_citras":
				#esta opcion es para llenar la datable.
				
				# se crean variables vanderas para evitar que truene el sistema
				exito, mensaje, objecto, lista_resulto = False, 'error', {}, []
				
				# se hace un aconsulta a la tabla DatosResidente y se extraen todos los datos. 
				consulta = DatosResidente.objects.all()
				
				# se hace un conteo de registros obtenidos de la consulta para mostrarlo en la parte de abajo de la datatable
				total = consulta.count()

				# la datable lanza esos parametros en el POST iDisplayStart y iDisplayLength para la opcion de 20,50.100 registros en la tabla
				start = int(request.POST.get('iDisplayStart'))
				length = int(request.POST.get('iDisplayLength'))
				consulta_bdatos = consulta[start:start+length]
				
				# Se hace un for para datos del queryset de la consulta.
				for columna in consulta_bdatos:
					# Por cada recorrido en dato lo agrega al array lista_resulto[] con metodo append() 
					lista_resulto.append([
						columna.residente,
						columna.escuela,
						columna.fecha,
					])
				# Los actualiza los datos obtenido   
				objecto.update({'aaData': lista_resulto, 'iTotalRecords': total, 'iTotalDisplayRecords': total,})
				#El diccionario que retornas contiene:
				contexto.update({
					'exito': exito,
					'mensaje': mensaje,
					'objecto': objecto
				})
			return JsonResponse(contexto)
		elif request.method == 'GET':
			return render(request, 'paginas/ver_citas.html')
	except Exception as e:
		print('Excepción en la vista de ver citas => {}'.format(str(e)))
	return render(request, 'paginas/ver_citas.html')




#-----------Vista donde subiran los proyectos los administradores------------
def subir_proyectos(request):
	try:
		if request.method == 'POST':
			img = request.FILES.get('proyecto')
			username = User(request.user.id)
			proyectonombre = request.POST['nombre']
			area = request.POST['area']
			cantidad = request.POST['cantidadr']
			if img:
				model_media = Administradores.objects.create(
					nombre=proyectonombre,
					area=area,
					cantidad=cantidad,
					proyecto=img,
					user=username
				)
				model_media.save()
		elif request.method == 'GET':
			return render(request, 'paginas/subir_proyectos.html')
	except Exception as e:
			print('Excepción en la vista subir_proyectos => {}'. format(e.args))
	return render(request, 'paginas/subir_proyectos.html')

#-----------Vista donde consultaran los proyectos que seleccionen los residentes ------------
def consultar_proyectos(request):
	return render(request, 'paginas/consultar_proyectos.html')

#-----------Vista donde veran los admins y rh los residentes registrados------------
def ver_residentes(request, *args, **kwargs):
	contexto = {}
	try:
		if request.method == 'POST' and request.is_ajax():
			#En cada petion  ajax a la vista se incluye la accion a realizar con la variable opccion
			opccion = request.POST.get('opccion')
			#evaluas que quieres hacer con la variable option
			if opccion == "agendar_cita":
        # Aqui puedes replicar el proceso en la peticiones ajax que hagas y solo los datos los retornas en el json responso con
        # la misma estrucutra del contexto
				pass

			elif opccion == "datable_citras":
				#esta opcion es para llenar la datable.
				
				# se crean variables vanderas para evitar que truene el sistema
				exito, mensaje, objecto, lista_resulto = False, 'error', {}, []
				
				# se hace un aconsulta a la tabla DatosResidente y se extraen todos los datos. 
				consulta = Residente.objects.all()
				
				# se hace un conteo de registros obtenidos de la consulta para mostrarlo en la parte de abajo de la datatable
				total = consulta.count()

				# la datable lanza esos parametros en el POST iDisplayStart y iDisplayLength para la opcion de 20,50.100 registros en la tabla
				start = int(request.POST.get('iDisplayStart'))
				length = int(request.POST.get('iDisplayLength'))
				consulta_bdatos = consulta[start:start+length]
				
				# Se hace un for para datos del queryset de la consulta.
				for columna in consulta_bdatos:
					# Por cada recorrido en dato lo agrega al array lista_resulto[] con metodo append() 
					lista_resulto.append([
						columna.nombre,
						columna.usuario.first_name,
						columna.usuario.last_name,
						columna.escuela,
						columna.telefono,
						columna.usuario.username
					])
				# Los actualiza los datos obtenido   
				objecto.update({'aaData': lista_resulto, 'iTotalRecords': total, 'iTotalDisplayRecords': total,})
				#El diccionario que retornas contiene:
				contexto.update({
					'exito': exito,
					'mensaje': mensaje,
					'objecto': objecto
				})
			return JsonResponse(contexto)
		elif request.method == 'GET':
			return render(request, 'paginas/ver_residentes.html')
	except Exception as e:
		print('Excepción en la vista de ver residentes => {}'.format(str(e)))
	return render(request, 'paginas/ver_residentes.html')

#-----------Vista donde subiran los proyectos los administradores------------
def documentos_residentes(request):
	return render(request, 'paginas/documentos_residentes.html')




