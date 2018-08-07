from sumeyyeozkaynak.settings.base import *

DEBUG = True
ALLOWED_HOSTS=['www.sumeyyeozkaynak.me', 'sumeyyeozkaynak.me','188.166.68.147']


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

NOCAPTCHA = True
