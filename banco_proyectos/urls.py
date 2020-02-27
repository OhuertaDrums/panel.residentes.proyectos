from django.urls import path

from . import views

app_name = 'banco_proyectos	'
urlpatterns = [

    path('', views.bienvenido, name='bienvenido'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

    path('vistaprincipal', views.vistaprincipal, name='vistaprincipal'), 
    path('registrar', views.registrar, name='registrar'),
    path('agendar', views.agendar, name='agendar'),
    path('residentes', views.residentes, name='residentes'),
    path('archivosr', views.archivosr, name= 'archivosr'),
    path('restablecer-contraseña', views.restablecercontraseña, name= 'restablecer'),
    path('verproyectos', views.verproyectos, name= 'proyectos'),
    path('agregar_usuario', views.agregar_usuario, name= 'agregar_usuario'),
    #Urls para la seccioón de los administradores
    path('subir-proyectos', views.subir_proyectos, name= 'subir_proyectos'),
    path('panel-administrativo', views.panel_administradores, name= 'panel_administradores'),
    path('ver-citas', views.ver_citas, name= 'ver_citas'),
    path('consultar-proyectos-seleccionados', views.consultar_proyectos, name= 'consultar_proyectos'),
    path('residentes-registrados', views.ver_residentes, name= 'ver_residentes'),
    path('documentos-residentes', views.documentos_residentes, name= 'documentos_residentes'),

    


]