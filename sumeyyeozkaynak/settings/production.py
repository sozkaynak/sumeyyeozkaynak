from sumeyyeozkaynak.settings.base import *
DEBUG = False

ALLOWED_HOST=['www.sumeyyeozkaynak.me','sumeyyeozkaynak.me']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_sumeyyeozkaynak',
        'USER': 'sumeyyeozkaynak',
        'PASSWORD': 'djsmyyzkynkpassword',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
