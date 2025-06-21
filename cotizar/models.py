# landing/models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils import timezone

class Servicio(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del servicio")
    descripcion = models.TextField(verbose_name="Descripción")
    precio = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name="Precio base (COP)"
    )
    requiere_ia = models.BooleanField(
        default=False,
        verbose_name="Requiere IA"
    )
    impacto_precio = models.CharField(
        max_length=50,
        choices=[
            ('Bajo', 'Bajo (+0%)'),
            ('Medio', 'Medio (+20%)'),
            ('Alto', 'Alto (+50%)')
        ],
        verbose_name="Impacto en precio"
    )

    def __str__(self):
        return f"{self.nombre} - ${self.precio:,.2f} COP"

    def calcular_precio_final(self, descuento=0):
        """Calcula precio con ajustes por impacto y descuento"""
        multiplicador = {
            'Bajo': 1.0,
            'Medio': 1.2,
            'Alto': 1.5
        }.get(self.impacto_precio, 1.0)
        
        precio_ajustado = self.precio * multiplicador
        return precio_ajustado * (1 - float(descuento)/100)

class Cotizacion(models.Model):
    nombre_cliente = models.CharField(
        max_length=100,
        verbose_name="Nombre completo"
    )
    email = models.EmailField(verbose_name="Correo electrónico")
    servicio = models.ForeignKey(
        Servicio,
        on_delete=models.CASCADE,
        verbose_name="Servicio solicitado"
    )
    cantidad = models.PositiveIntegerField(
        default=1,
        verbose_name="Cantidad"
    )
    descuento = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        verbose_name="Descuento (%)"
    )
    mensaje = models.TextField(
        blank=True,
        verbose_name="Mensaje adicional"
    )
    fecha = models.DateTimeField(
        default=timezone.now,
        verbose_name="Fecha de solicitud"
    )
    enviado = models.BooleanField(
        default=False,
        verbose_name="¿Respuesta enviada?"
    )

    class Meta:
        verbose_name = "Cotización"
        verbose_name_plural = "Cotizaciones"
        ordering = ['-fecha']

    def __str__(self):
        return f"Cotización #{self.id} - {self.nombre_cliente}"

    @property
    def precio_total(self):
        """Calcula el total con descuento y cantidad"""
        return self.servicio.calcular_precio_final(self.descuento) * self.cantidad

    def clean(self):
        """Valida el descuento máximo permitido"""
        if float(self.descuento) < 0 or float(self.descuento) > 30:  # Máximo 30% de descuento
            raise ValidationError("El descuento debe estar entre 0% y 30%")

    def enviar_respuesta_automatica(self):
        """Envía email con la cotización calculada"""
        if not self.enviado:  # Evita reenvíos
            subject = f"📄 Cotización {self.id} - {self.servicio.nombre}"
            context = {
                'cotizacion': self,
                'precio_unitario': self.servicio.calcular_precio_final(self.descuento),
                'fecha': timezone.localtime(self.fecha).strftime("%d/%m/%Y %H:%M")
            }
            
            message = render_to_string('emails/cotizacion_automatica.html', context)
            
            send_mail(
                subject,
                message,
                'cotizaciones@tudominio.com',
                [self.email],
                html_message=message,
                fail_silently=False,
            )
            
            self.enviado = True
            self.save()

    def save(self, *args, **kwargs):
        """Valida antes de guardar"""
        self.full_clean()
        super().save(*args, **kwargs)