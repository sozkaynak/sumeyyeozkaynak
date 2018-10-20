from sumeyyeozkaynak.settings.base import *
DEBUG = True
ALLOWED_HOSTS=[]

#DATABASES = {
#    'default': {
 #       'ENGINE': 'django.db.backends.sqlite3',
  #      'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
   # }
#}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_website',
        'USER': 'sumeyyeozkaynak',
        'PASSWORD': '203948',
        'HOST': 'localhost',
        'PORT': '',
    }
}


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

NOCAPTCHA = False
