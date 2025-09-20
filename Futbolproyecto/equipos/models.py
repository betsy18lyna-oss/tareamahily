from django.db import models
# Create your models here.

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    estadio = models.CharField(max_length=100)
    fundacion = models.IntegerField()

    def __str__(self):
        return self.nombre