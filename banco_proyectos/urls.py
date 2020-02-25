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


]