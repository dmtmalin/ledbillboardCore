# -*- coding: utf-8 -*-
import os

DEBUG = False

ALLOWED_HOSTS = ['*']

# Timezone
TIME_ZONE = 'Europe/Moscow'

# База данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
    }
}

# Путь по которому раздаётся статика приложения
STATIC_ROOT = '/var/www/board/static/'


WEBDAV_URL = os.environ.get('WEBDAV_URL')
WEBDAV_PUBLIC_URL = os.environ.get('WEBDAV_PUBLIC_URL')
