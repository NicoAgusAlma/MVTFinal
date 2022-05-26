from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    mail=models.EmailField()
    password=models.CharField(max_length=40)
    nacimiento=models.DateField()

class Direccion(models.Model):
    pais=models.CharField(max_length=40)
    provincia=models.CharField(max_length=40)
    localidad=models.CharField(max_length=40)
    calle=models.CharField(max_length=40)
    numero=models.IntegerField()
  
class Estudio(models.Model):
    institucion=models.CharField(max_length=40)
    carrera=models.CharField(max_length=40)
    tiempoCursado=models.IntegerField()
    egresado=models.BooleanField()
   