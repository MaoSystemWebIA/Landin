from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactoForm

def landing_page(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            contacto = form.save()
            # Enviar correo automático
            send_mail(
                'Nuevo contacto desde MaoSystemWebIA',
                f'Nombre: {contacto.nombre}\nEmail: {contacto.email}\nServicio: {contacto.servicio}\nRequiere IA: {contacto.requiere}\nTecnología: {contacto.tecnologia_cliente}\nMensaje: {contacto.mensaje}',
                'maosystem1@gmail.com',
                ['maosystem1@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'landing_page/gracias.html')
    else:
        form = ContactoForm()
    return render(request, 'landing_page/landing_page.html', {'form': form})
