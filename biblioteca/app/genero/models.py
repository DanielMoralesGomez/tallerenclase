from django.db import models


class Genero(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.nombre

