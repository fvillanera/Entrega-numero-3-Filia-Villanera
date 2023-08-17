from django.db import models

# Create your models here.

class Curso (models.Model):
    nombre = models.CharField(max_length=50)
    comision  = models.IntegerField()
    def __str__ (self):
        return f"{self.nombre} / Comision: {self.comision}"
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    #hobbie= models.CharField(max_length=50)
    def __str__ (self):
        return f"{self.nombre}, {self.apellido}"
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)
    def __str__ (self):
        return f"{self.nombre}, {self.apellido}"
    
    class Meta:
        verbose_name = "profesor"
        verbose_name_plural = "profesores"
        ordering = ["apellido"]
    

class Fechaproxima(models.Model):
    nombre = models.CharField(max_length=50)
    fechaProxima = models.DateField()
    
    def __str__(self):
        return f"{self.fechaProxima}, {self.fechaProxima}"
    class Meta:
        verbose_name = "fecha proxima"
        verbose_name_plural = "fechas proximas"