from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    servicio = models.CharField(max_length=100)
    requiere = models.BooleanField(default=False)
    tecnologia_cliente = models.CharField(max_length=100, blank=True)
    mensaje = models.TextField(blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.servicio}"
