<<<<<<< HEAD
# Landin
Landin Page IA para prestar servicios relacionados con IA 
Despliegue

Esta aplicación está desplegada usando [Railway](https://railway.app), una plataforma de infraestructura moderna y sencilla.

Puedes ver el proyecto en vivo aquí: [https://mi-app.up.railway.app](https://mi-app.up.railway.app)
=======
# Landin - Sistema Web IA

Proyecto Django con aplicaciones de inteligencia artificial para marketing y asistencia virtual.

## 🚀 Despliegue en Railway

### Requisitos Previos
- Cuenta en [Railway](https://railway.app)
- Repositorio en GitHub con el código del proyecto

### Pasos para Desplegar

1. **Conectar Repositorio**
   - Ve a Railway Dashboard
   - Haz clic en "New Project"
   - Selecciona "Deploy from GitHub repo"
   - Conecta tu repositorio `MaoSystemWebIA/Landin`

2. **Configurar Variables de Entorno**
   En Railway, ve a la pestaña "Variables" y configura:
   ```
   SECRET_KEY=tu_clave_secreta_muy_larga_y_compleja
   DEBUG=False
   ALLOWED_HOSTS=localhost,127.0.0.1,.railway.app
   ```

3. **Configurar Base de Datos**
   - En Railway, ve a "New Service" → "Database" → "PostgreSQL"
   - Railway automáticamente configurará `DATABASE_URL`
   - Las migraciones se ejecutarán automáticamente

4. **Desplegar**
   - Railway detectará automáticamente el Dockerfile
   - El build comenzará automáticamente
   - La aplicación estará disponible en la URL proporcionada por Railway

### Estructura del Proyecto

```
Landin/
├── mysitioweb/          # Configuración principal de Django
├── landing_page/        # Página de inicio y formulario de contacto
├── cotizar/            # Aplicación de cotizaciones
├── Marketing_IA/       # Herramientas de marketing con IA
├── asistente_virtual_IA/ # Asistente virtual
├── static/             # Archivos estáticos (CSS, JS, imágenes)
├── templates/          # Plantillas HTML
├── Dockerfile          # Configuración para Railway
├── railway.json        # Configuración específica de Railway
├── requirements.txt    # Dependencias de Python
└── run_waitress.py     # Servidor de producción
```

### Solución de Problemas

#### Error: "Se produjo un error al implementar desde la fuente"

1. **Revisar Logs**: Ve a Railway → Tu proyecto → Deployments → Ver logs del último deployment
2. **Verificar Variables**: Asegúrate de que todas las variables de entorno estén configuradas
3. **Verificar Base de Datos**: Confirma que PostgreSQL esté configurado correctamente

#### Variables de Entorno Requeridas
- `SECRET_KEY`: Clave secreta de Django (generar una nueva para producción)
- `DEBUG`: False para producción
- `ALLOWED_HOSTS`: Incluir el dominio de Railway
- `DATABASE_URL`: Configurado automáticamente por Railway

### Tecnologías Utilizadas
- **Backend**: Django 5.2.1
- **Base de Datos**: PostgreSQL
- **Servidor**: Waitress
- **Plataforma**: Railway
- **Contenedorización**: Docker

### Contacto
Para soporte técnico, revisa los logs de Railway o contacta al equipo de desarrollo.

# Proyecto Landin

Este es un resumen del proyecto...
(Nueva información combinada)
>>>>>>> c7e120c ( cambios realizados para futuras implementaciones)
