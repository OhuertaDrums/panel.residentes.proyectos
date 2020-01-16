from django.urls import path

from . import views

app_name = 'banco_proyectos	'
urlpatterns = [

    path('login', views.login, name='login'),
    path('vistaprincipal', views.vistaprincipal, name='vistaprincipal'), 
    path('registrar', views.registrar, name='registrar'),
    path('agendar', views.agendar, name='agendar'),
    path('residentes', views.residentes, name='residentes'),
    path('archivosr', views.archivosr, name= 'archivosr'),
    path('restablecer-contraseña', views.restablecercontraseña, name= 'restablecer'),


]