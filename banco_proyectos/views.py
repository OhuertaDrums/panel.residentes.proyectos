from django.shortcuts import render



from django.http import HttpResponse


def index(request):
    return HttpResponse(" Bienvenido al Banco de Proyectos FINKOK")

