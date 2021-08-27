# production.py
from .base import *

import dj_database_url
import django_heroku

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django-site',
        'USER': 'name',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
django_heroku.settings(locals())


#STATIC_URL = 'https://nombreurlproyecto.com/static/'
#MEDIA_URL = 'https://nombreurlproyecto.com/media/'