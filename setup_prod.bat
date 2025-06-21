@echo off
echo Iniciando configuracion de produccion...

REM 1. Crear y activar entorno virtual
echo Creando entorno virtual...
python -m venv .venv_prod
call .venv_prod\Scripts\activate

REM 2. Instalar dependencias
echo Instalando dependencias...
pip install -r requirements_prod.txt

REM 3. Crear archivo .env
echo Creando archivo .env...
(
echo DB_NAME=Landin
echo DB_USER=postgres
echo DB_PASSWORD=1234qwertymao
echo DB_HOST=localhost
echo DB_PORT=5432
echo EMAIL_HOST_USER=maosystem1@gmail.com
echo EMAIL_HOST_PASSWORD=tu_contraseña_email
) > .env

REM 4. Aplicar migraciones
echo Aplicando migraciones...
python manage.py migrate

REM 5. Recolectar archivos estáticos
echo Recolectando archivos estaticos...
python manage.py collectstatic --noinput

REM 6. Crear directorio de logs
echo Creando directorio de logs...
if not exist logs mkdir logs
type nul > logs\django.log

echo Configuracion completada!
echo Por favor, verifica los siguientes puntos:
echo 1. Asegurate de que PostgreSQL esta corriendo
echo 2. Verifica que los puertos 80 y 443 estan abiertos
echo 3. Configura tu certificado SSL
echo 4. Ajusta las rutas en apache/maosystem.conf segun tu sistema

pause 