# MaoSystemWebIA — Consultoría Freelance Full-Stack, Cloud & IA

![Django](https://img.shields.io/badge/Django-5.2.1-green.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Tailwind](https://img.shields.io/badge/Tailwind-CSS-38bdf8.svg)

Landing page profesional de **Andrés Mauricio Bohorquez Ortiz** — Ingeniero de Sistemas especializado en desarrollo Full-Stack (Python/Django), consultoría Cloud AWS e integración de Inteligencia Artificial.

Orientada a prestar servicios de **consultoría freelance** para empresas, startups y emprendimientos.

## Enlaces

- **GitHub Pages (estática):** [https://maosystemwebia.github.io/Landin](https://maosystemwebia.github.io/Landin)
- **Repositorio:** [https://github.com/MaoSystemWebIA/Landin](https://github.com/MaoSystemWebIA/Landin)
- **Portafolio:** [https://github.com/maoSystemWebIA](https://github.com/maoSystemWebIA)

## Servicios

- Desarrollo Full-Stack (Python, Django, PostgreSQL, APIs REST)
- Consultoría Cloud (AWS, SageMaker, Bedrock)
- Soluciones con IA (ML, IA generativa, prompt engineering)
- Administración y optimización de bases de datos
- Desarrollo web (landing pages, WordPress)
- Asistentes virtuales y chatbots con IA

## Características

- Landing page con marca personal y experiencia profesional
- Formulario de contacto Django con persistencia en base de datos
- Botón de contacto directo por WhatsApp
- Demo interactivo de asistente virtual (AsistenteX)
- Diseño responsivo con Tailwind CSS
- Versión estática sincronizada para GitHub Pages

## Tecnologías

### Backend
- Django 5.2.1
- Python 3.8+
- SQLite

### Frontend
- HTML5 / CSS3 / JavaScript
- Tailwind CSS (CDN)
- Font Awesome

### Despliegue
- GitHub Pages (`index.html`)
- Railway / Docker (Django + Waitress)

## Estructura del proyecto

```
Landin/
├── mysitioweb/              # Configuración Django
├── landing_page/            # Landing y formulario de contacto
├── cotizar/                 # Sistema de cotizaciones
├── Marketing_IA/            # Herramientas de marketing con IA
├── asistente_virtual_IA/      # Asistente virtual
├── templates/               # Plantillas HTML
├── static/                  # CSS e imágenes
├── index.html               # Versión estática (GitHub Pages)
└── manage.py
```

## Instalación local

```bash
git clone https://github.com/MaoSystemWebIA/Landin.git
cd Landin
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
cp env.example env_local      # Configurar variables
python manage.py migrate
python manage.py runserver
```

Accede en: http://127.0.0.1:8000/

## Contacto

- **Email:** maosystem1@gmail.com
- **WhatsApp:** +57 316 943 8662
- **LinkedIn:** [mauricio-bohorquez-43495749](https://www.linkedin.com/in/mauricio-bohorquez-43495749/)

## Licencia

MIT — ver archivo [LICENSE](LICENSE).
