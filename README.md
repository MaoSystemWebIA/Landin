# MaoSystemWebIA - Sistema Web con Inteligencia Artificial

![Django](https://img.shields.io/badge/Django-5.2.1-green.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supported-blue.svg)
![Railway](https://img.shields.io/badge/Deploy-Railway-orange.svg)

Un sistema web completo desarrollado en Django que ofrece servicios relacionados con Inteligencia Artificial, incluyendo marketing digital, cotizaciones y asistente virtual.

## 🌟 Características Principales

- **Landing Page Dinámica**: Página de inicio con formulario de contacto integrado
- **Sistema de Cotizaciones**: Generación automática de cotizaciones para servicios de IA
- **Marketing con IA**: Herramientas de marketing digital potenciadas por inteligencia artificial
- **Asistente Virtual**: Chatbot inteligente para atención al cliente
- **Diseño Responsivo**: Interfaz moderna y adaptable a todos los dispositivos
- **Base de Datos PostgreSQL**: Configuración optimizada para producción
- **Despliegue Automático**: Configurado para Railway con Docker

## 🚀 Versiones Disponibles

### 🌐 Versión Dinámica (Django)
- **URL**: [https://maosystemwebia-production.up.railway.app](https://maosystemwebia-production.up.railway.app)
- **Características**: Funcionalidad completa con base de datos, formularios dinámicos y todas las aplicaciones

### 📄 Versión Estática (GitHub Pages)
- **URL**: [https://maosystemwebia.github.io/Landin](https://maosystemwebia.github.io/Landin)
- **Características**: Landing page estática para demostración rápida

## 🛠️ Tecnologías Utilizadas

### Backend
- **Django 5.2.1**: Framework web principal
- **Python 3.8+**: Lenguaje de programación
- **PostgreSQL**: Base de datos de producción
- **SQLite**: Base de datos de desarrollo

### Frontend
- **HTML5/CSS3**: Estructura y estilos
- **JavaScript**: Interactividad del cliente
- **Bootstrap**: Framework CSS responsivo

### Despliegue
- **Railway**: Plataforma de hosting principal
- **Docker**: Contenedorización
- **Waitress**: Servidor WSGI de producción
- **GitHub Pages**: Hosting estático

## 📁 Estructura del Proyecto

```
MaoSystemWebIA/
├── mysitioweb/              # Configuración principal de Django
│   ├── settings.py          # Configuración de desarrollo
│   ├── settings_prod.py     # Configuración de producción
│   ├── urls.py              # URLs principales
│   └── wsgi.py              # Configuración WSGI
├── landing_page/            # Aplicación de página de inicio
│   ├── models.py            # Modelo de contacto
│   ├── views.py             # Vistas de la landing page
│   ├── forms.py             # Formularios
│   └── urls.py              # URLs de la aplicación
├── cotizar/                 # Sistema de cotizaciones
├── Marketing_IA/            # Herramientas de marketing con IA
├── asistente_virtual_IA/    # Asistente virtual
├── static/                  # Archivos estáticos (CSS, JS, imágenes)
├── templates/               # Plantillas HTML
├── staticfiles/             # Archivos estáticos recolectados
├── Dockerfile               # Configuración Docker
├── railway.json             # Configuración Railway
├── requirements.txt         # Dependencias de Python
├── requirements_prod.txt    # Dependencias de producción
├── Procfile                 # Configuración para Heroku
├── run_waitress.py          # Servidor de producción
├── setup_prod.sh           # Script de configuración Linux
├── setup_prod.bat          # Script de configuración Windows
└── index.html              # Versión estática para GitHub Pages
```

## 🚀 Instalación Local

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/maosystemwebia/Landin.git
   cd Landin
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # Linux/Mac
   source .venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**
   ```bash
   # Copiar archivo de ejemplo
   cp env.example env_local
   
   # Editar variables en env_local
   SECRET_KEY=tu_clave_secreta_aqui
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   DATABASE_URL=sqlite:///db.sqlite3
   ```

5. **Ejecutar migraciones**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Crear superusuario (opcional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Ejecutar servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

8. **Acceder a la aplicación**
   - URL principal: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## 🌐 Despliegue en Railway

### Configuración Automática

1. **Conectar con GitHub**
   - Ve a [Railway Dashboard](https://railway.app)
   - Crea nuevo proyecto
   - Selecciona "Deploy from GitHub repo"
   - Conecta tu repositorio `maosystemwebia/Landin`

2. **Variables de Entorno Requeridas**
   ```
   SECRET_KEY=tu_clave_secreta_muy_larga_y_compleja
   DEBUG=False
   ALLOWED_HOSTS=localhost,127.0.0.1,.railway.app
   ```

3. **Base de Datos PostgreSQL**
   - Railway configurará automáticamente `DATABASE_URL`
   - Las migraciones se ejecutarán automáticamente

### Configuración Manual

Si prefieres configuración manual:

1. **Crear servicio de base de datos**
   - New Service → Database → PostgreSQL

2. **Configurar variables de entorno**
   - Ve a la pestaña "Variables"
   - Agrega todas las variables requeridas

3. **Desplegar**
   - Railway detectará el Dockerfile automáticamente
   - El build comenzará automáticamente

## 🔧 Configuración de Producción

### Variables de Entorno de Producción
```bash
SECRET_KEY=clave_secreta_muy_larga_y_compleja
DEBUG=False
ALLOWED_HOSTS=tu-dominio.railway.app,localhost,127.0.0.1
DATABASE_URL=postgresql://usuario:password@host:puerto/database
```

### Comandos de Producción
```bash
# Recolectar archivos estáticos
python manage.py collectstatic --noinput

# Ejecutar migraciones
python manage.py migrate

# Ejecutar servidor de producción
python run_waitress.py
```

## 📱 Aplicaciones del Sistema

### 1. Landing Page (`landing_page`)
- Página de inicio con diseño moderno
- Formulario de contacto integrado
- Información de servicios de IA
- Diseño responsivo

### 2. Sistema de Cotizaciones (`cotizar`)
- Generación automática de cotizaciones
- Cálculo de precios para servicios de IA
- Formularios personalizados
- Historial de cotizaciones

### 3. Marketing con IA (`Marketing_IA`)
- Herramientas de marketing digital
- Análisis de datos con IA
- Generación de contenido
- Optimización de campañas

### 4. Asistente Virtual (`asistente_virtual_IA`)
- Chatbot inteligente
- Atención al cliente automatizada
- Respuestas contextuales
- Integración con servicios de IA

## 🐛 Solución de Problemas

### Error: "Se produjo un error al implementar desde la fuente"

1. **Revisar Logs de Railway**
   - Ve a Railway → Tu proyecto → Deployments
   - Revisa los logs del último deployment

2. **Verificar Variables de Entorno**
   - Confirma que todas las variables estén configuradas
   - Verifica que `SECRET_KEY` sea válida

3. **Verificar Base de Datos**
   - Confirma que PostgreSQL esté configurado
   - Verifica que `DATABASE_URL` sea correcta

### Error: "ModuleNotFoundError"

1. **Verificar requirements.txt**
   ```bash
   pip install -r requirements.txt
   ```

2. **Verificar entorno virtual**
   ```bash
   # Activar entorno virtual
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate     # Windows
   ```

### Error: "Database connection failed"

1. **Verificar configuración de base de datos**
   - Confirma que PostgreSQL esté ejecutándose
   - Verifica credenciales en `DATABASE_URL`

2. **Ejecutar migraciones**
   ```bash
   python manage.py migrate
   ```

## 🔒 Seguridad

- **SECRET_KEY**: Generada automáticamente para producción
- **DEBUG**: Deshabilitado en producción
- **ALLOWED_HOSTS**: Configurado para dominios específicos
- **CSRF Protection**: Habilitado por defecto
- **HTTPS**: Configurado automáticamente en Railway

## 📊 Monitoreo y Logs

### Railway Logs
- Accede a Railway Dashboard
- Ve a tu proyecto → Deployments
- Revisa logs en tiempo real

### Django Logs
```bash
# Ver logs de Django
python manage.py runserver --verbosity=2
```

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Contacto

- **Proyecto**: [MaoSystemWebIA](https://github.com/maosystemwebia/Landin)
- **Versión Dinámica**: [https://maosystemwebia-production.up.railway.app](https://maosystemwebia-production.up.railway.app)
- **Versión Estática**: [https://maosystemwebia.github.io/Landin](https://maosystemwebia.github.io/Landin)

## 🙏 Agradecimientos

- Django Framework
- Railway Platform
- PostgreSQL Database
- Bootstrap CSS Framework
- Python Community

---

**Desarrollado con ❤️ usando Django y Python**
