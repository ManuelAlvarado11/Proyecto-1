from django.db import models

# Create your models here.

class Usuario(models.model):
	nombre = models.TextField()
	apellido = models.TextField()
	usuario = models.TextField()
	password = models.TextField()