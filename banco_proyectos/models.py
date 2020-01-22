from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class residente(models.Model):
	telefono = models.CharField( max_length=30)
	escuela = models.CharField(max_length=50)