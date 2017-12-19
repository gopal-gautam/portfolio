from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'temp/db.sqlite3'),
    }
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'gopalgautam.mailgateway@gmail.com'
EMAIL_HOST_PASSWORD = 'thegreat'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER