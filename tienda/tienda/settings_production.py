import os
from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Permitir tu dominio de PythonAnywhere
ALLOWED_HOSTS = ['velour.pythonanywhere.com']  # Cambiar 'tuusuario' por tu nombre de usuario

# Base de datos para producción (MySQL en PythonAnywhere)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'velour$tienda',  # Cambiar 'tuusuario' por tu nombre de usuario
        'USER': 'velour',        # Cambiar 'tuusuario' por tu nombre de usuario
        'PASSWORD': 'Gonzalo43878451.',  # Lo configuraremos más tarde
        'HOST': 'velour.mysql.pythonanywhere-services.com',  # Cambiar 'tuusuario'
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# Configuración de archivos estáticos y media para PythonAnywhere
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/velour/mysite/media/'  # Cambiar 'tuusuario' por tu nombre de usuario

# Configuración adicional de seguridad
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True