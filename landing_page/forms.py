from django import forms
from .models import Contacto

SERVICIO_CHOICES = [
    ('', 'Selecciona un servicio'),
    ('Desarrollo Full-Stack', 'Desarrollo Full-Stack'),
    ('Consultoría Cloud (AWS)', 'Consultoría Cloud (AWS)'),
    ('Soluciones con IA', 'Soluciones con IA'),
    ('Bases de Datos', 'Bases de Datos'),
    ('Desarrollo Web', 'Desarrollo Web'),
    ('Asistentes virtuales', 'Asistentes virtuales'),
    ('Otro', 'Otro'),
]


class ContactoForm(forms.ModelForm):
    servicio = forms.ChoiceField(
        choices=SERVICIO_CHOICES,
        label='Servicio de interés',
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
        }),
    )

    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'servicio', 'requiere', 'tecnologia_cliente', 'mensaje']
        labels = {
            'nombre': 'Nombre',
            'email': 'Correo electrónico',
            'requiere': '¿Requiere integración con IA?',
            'tecnologia_cliente': 'Tecnología o stack actual del proyecto',
            'mensaje': 'Mensaje',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Tu nombre',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'tu@email.com',
            }),
            'tecnologia_cliente': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Ej. Python, WordPress, AWS...',
            }),
            'mensaje': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 min-h-[150px] resize-y',
                'placeholder': 'Cuéntame sobre tu proyecto...',
                'rows': 6,
            }),
            'requiere': forms.CheckboxInput(attrs={
                'class': 'w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500',
            }),
        }
