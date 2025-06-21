import os
import sys
from django.core.wsgi import get_wsgi_application

# Añadir el directorio del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cotizar.settings')

application = get_wsgi_application() 