from django.db import models
from apps.vehiculo.models import Vehiculo
from app.sistemaFreno.models import SistemaFreno

# Create your models here.

class Prueba(models.Model):
	velocidad_inicial = models.DecimalField( max_digits=5, decimal_places=2)
    tiempo_frenado = models.DecimalField( max_digits=5, decimal_places=2)
    distancia de frenado = models.DecimalField(max_digits=7, decimal_places=2)
    fuerzaPedal = models.DecimalField( max_digits=5, decimal_places=2)
    vehiculo = models.ForeingnKey(Vehiculo, null=True, blank=True, on_delete=models.CASCADE) 
    sistemaFreno = models.ForeingKey(SistemaFreno, null=True, blank= True, on_delete=models.CASCADE)
    