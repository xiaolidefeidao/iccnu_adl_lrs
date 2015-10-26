# settings_prod.py
import os

from settings import *

print 'running in production mode'

DEBUG = TEMPLATE_DEBUG = False
SITE_DOMAIN = 'lrs.iccnu.net:80'
STATIC_URL = os.environ['STATIC_URL']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lrs',
        'USER': os.environ['DB_USER'],
        'PASSWORD':  os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['DB_PORT'],
    }
}
