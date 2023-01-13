from django.db import models


class Medidor(models.Model):
    """ Retorna la llave y el nombre del medidor"""

    llave = models.CharField(max_length=255, unique=True)
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Medicion(models.Model):
    """Retorna los valores de consumo del medidor"""

    medidor = models.ForeignKey(Medidor, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    consumo = models.PositiveIntegerField()

    def __str__(self):
        return self.medidor
