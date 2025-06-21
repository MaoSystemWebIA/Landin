#!/bin/bash

# Colores para mensajes
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${GREEN}Iniciando configuración de producción...${NC}"

# 1. Crear y activar entorno virtual
echo -e "${GREEN}Creando entorno virtual...${NC}"
python -m venv .venv_prod
source .venv_prod/bin/activate

# 2. Instalar dependencias
echo -e "${GREEN}Instalando dependencias...${NC}"
pip install -r requirements_prod.txt

# 3. Crear archivo .env
echo -e "${GREEN}Creando archivo .env...${NC}"
cat > .env << EOL
DB_NAME=Landin
DB_USER=postgres
DB_PASSWORD=1234qwertymao
DB_HOST=localhost
DB_PORT=5432
EMAIL_HOST_USER=maosystem1@gmail.com
EMAIL_HOST_PASSWORD=tu_contraseña_email
EOL

# 4. Aplicar migraciones
echo -e "${GREEN}Aplicando migraciones...${NC}"
python manage.py migrate

# 5. Recolectar archivos estáticos
echo -e "${GREEN}Recolectando archivos estáticos...${NC}"
python manage.py collectstatic --noinput

# 6. Crear directorio de logs
echo -e "${GREEN}Creando directorio de logs...${NC}"
mkdir -p logs
touch logs/django.log

# 7. Configurar Apache
echo -e "${GREEN}Configurando Apache...${NC}"
sudo cp apache/maosystem.conf /etc/apache2/sites-available/
sudo a2ensite maosystem.conf
sudo a2enmod ssl
sudo a2enmod rewrite

# 8. Reiniciar Apache
echo -e "${GREEN}Reiniciando Apache...${NC}"
sudo systemctl restart apache2

echo -e "${GREEN}¡Configuración completada!${NC}"
echo -e "Por favor, verifica los siguientes puntos:"
echo -e "1. Asegúrate de que PostgreSQL está corriendo"
echo -e "2. Verifica que los puertos 80 y 443 están abiertos"
echo -e "3. Configura tu certificado SSL"
echo -e "4. Ajusta las rutas en apache/maosystem.conf según tu sistema" 