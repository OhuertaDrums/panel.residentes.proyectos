from django.urls import path

from . import views

aap_name = 'banco_proyectos'

urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),

]