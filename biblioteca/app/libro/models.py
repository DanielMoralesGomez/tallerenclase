from django.db import models
from app.genero.models import Genero
from app.autor.models import Autor

class Libro(models.Model):
    titulo = models.CharField(max_length=300)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)  

    def __str__(self):
        return self.titulo
