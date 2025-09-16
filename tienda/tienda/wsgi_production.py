import os
import sys

# Agregar la ruta del proyecto
path = '/home/velour/tienda'  # Cambiar 'tuusuario' por tu nombre de usuario de PythonAnywhere
if path not in sys.path:
    sys.path.insert(0, path)

# Agregar la ruta de la carpeta tienda
path = '/home/velour/tienda/tienda'  # Cambiar 'tuusuario' por tu nombre de usuario
if path not in sys.path:
    sys.path.insert(0, path)

# Configurar Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'tienda.settings_production'

# Importar Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()