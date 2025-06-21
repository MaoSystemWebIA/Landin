from django import forms
from .models import Cotizacion, Servicio

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'precio', 'requiere_ia', 'impacto_precio']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'nombre': 'Nombre del Servicio',
            'descripcion': 'Descripción',
            'precio': 'Precio Base (COP)',
            'requiere_ia': '¿Requiere IA?',
            'impacto_precio': 'Impacto en el Precio',
        }


class CotizacionForm(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = ['nombre_cliente', 'email', 'servicio', 'cantidad', 'descuento', 'mensaje']
        widgets = {
            'mensaje': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'nombre_cliente': 'Nombre Completo',
            'email': 'Correo Electrónico',
            'servicio': 'Servicio Solicitado',
            'cantidad': 'Cantidad',
            'descuento': 'Descuento (%)',
            'mensaje': 'Mensaje Adicional',
        }

    def clean_descuento(self):
        descuento = self.cleaned_data.get('descuento')
        if descuento < 0 or descuento > 30:
            raise forms.ValidationError("El descuento debe estar entre 0% y 30%.")
        return descuento
