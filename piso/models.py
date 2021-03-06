from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from datetime import datetime  

class Piso(models.Model):
	user = models.CharField(max_length=100)
	Direccion = models.CharField(max_length=100)
	Precio = models.IntegerField(null=True)
	nombre = models.CharField(max_length=100)
	def __str__(self):
		return self.Direccion

class Gastosmensuales(models.Model):
	Mes = models.CharField(max_length=100)
	PrecioPiso = models.IntegerField(null=True)
	PrecioGas = models.IntegerField(null=True)
	PrecioLuz = models.IntegerField(null=True)
	PrecioInternet = models.IntegerField(null=True)
	PrecioTotal = models.IntegerField(null=True)
	Pisos=models.ForeignKey(Piso)
	def __str__(self):
		return self.PrecioTotal

class Tareas(models.Model):
	Limpieza = models.CharField(max_length=100)
	Basura = models.CharField(max_length=100)
	Extra = models.CharField(max_length=100)
	Semana = models.CharField(max_length=100)
	MesTarea = models.CharField(max_length=100)
	Pisos=models.ForeignKey(Piso)
	def __str__(self):
		return self.Semana

class Listacompra(models.Model):
	DineroPersona = models.IntegerField(null=True)
	Productos = models.TextField(max_length=700,null=True)
	fechalista = models.DateField(default=datetime.now, blank= True)
	Pisos=models.ForeignKey(Piso)

	def __str__(self):
		return self.DineroPersona

class Notas(models.Model):
	Texto = models.TextField(max_length=500,null=True)
	fecha = models.DateField(default=datetime.now, blank= True)
	Pisos=models.ForeignKey(Piso)
	def __str__(self):
		return self.Texto


