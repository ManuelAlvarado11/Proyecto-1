from django.db import models

# Create your models here.

class Disco(models.Model):
	diametro=models.DecimalField(max_digit)

class SistemaFreno(models.Model):
