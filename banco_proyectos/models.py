from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class residente(models.Model):
	usuario = models.OneToOneField(User, on_delete = models.CASCADE)
	telefono = models.CharField( max_length=30)
	escuela = models.CharField(max_length=50)
	nombre = models.CharField(max_length=50)