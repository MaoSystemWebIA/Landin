import os
from waitress import serve
from mysitioweb.wsgi import application

if __name__ == '__main__':
    # Railway asigna dinámicamente el puerto
    port = int(os.environ.get('PORT', 8000))
    # En Railway, necesitamos escuchar en 0.0.0.0, no en localhost
    serve(application, host='0.0.0.0', port=port) 