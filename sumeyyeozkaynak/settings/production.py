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

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

NOCAPTCHA = True
