from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Residente(models.Model):
	usuario = models.OneToOneField(User, on_delete = models.CASCADE)
	telefono = models.CharField( max_length=30)
	escuela = models.CharField(max_length=50)
	nombre = models.CharField(max_length=50)

class DatosResidente(models.Model):
	residente = models.CharField(max_length=50)
	escuela = models.CharField(max_length=50)
	fecha = models.CharField(max_length=25)
	