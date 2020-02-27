from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Residente(models.Model):
	usuario = models.OneToOneField(User, on_delete = models.CASCADE)
	telefono = models.CharField( max_length=30)
	escuela = models.CharField(max_length=50)
	nombre = models.CharField(max_length=50)

class DatosResidente(models.Model):
	usuario = models.OneToOneField(User, on_delete = models.CASCADE)
	residente = models.CharField(max_length=50)
	escuela = models.CharField(max_length=50)
	fecha = models.CharField(max_length=25)

class Archivos_residentes(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	acta_nacimiento = models.ImageField(upload_to='Actas_Nacimiento/')
	curp = models.ImageField(upload_to='Curp/')
	Ine = models.ImageField(upload_to='Ine/Ife/')
	domicilio = models.ImageField(upload_to='Comporbante_Domicilio/')
	comprobante_estudio = models.ImageField(upload_to='Comprobante_Estudios/')
	carta_presentación = models.ImageField(upload_to='Carta_Presentación/')
	certificado_medico = models.ImageField(upload_to='Certificado_Medico/')

class Administradores(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	nombre = models.CharField(max_length=80)
	area = models.CharField(max_length=80)
	cantidad = models.CharField(max_length=80)
	proyecto = models.ImageField(upload_to='proyectos/')




