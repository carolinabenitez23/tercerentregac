from django.db import models


class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    dni = models.IntegerField()
    
