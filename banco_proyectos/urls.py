from django.urls import path

from . import views

app_name = 'banco_proyectos	'
urlpatterns = [

    path('login', views.login, name='login'),
    path('vistaprincipal', views.vistaprincipal, name='vistaprincipal'), 
    path('registrar', views.registrar, name='registrar'),
    path('agendar', views.agendar, name='agendar'),
    path('residentes', views.residentes, name='residentes'),
    path('archivosresidente', views.archivosresidente, name= 'archivosresidente'),
    path('restablecer-contraseña', views.restablecercontraseña, name= 'restablecer'),


]