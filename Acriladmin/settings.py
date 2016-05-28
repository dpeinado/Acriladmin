"""
Django settings for Acriladmin project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import dj_database_url
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.contrib.admin import AdminSite
from django.contrib.auth.apps import AuthConfig

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zus&*yei-pwy*ov%$(3i*0@)b@4*7&gsdv__k5w(w(j*c98^0u'

# SECURITY WARNING: don't run with debug turned on in production!
IS_RUNNING_ON_HEROKU = "IS_RUNNING_ON_HEROKU" in os.environ
DEBUG = not IS_RUNNING_ON_HEROKU

if DEBUG:
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = ['*']
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cities_light',
    'back_office.apps.BackOfficeConfig',
    'finances.apps.FinancesConfig',
    'inventories.apps.InventoriesConfig',
    'operations.apps.OperationsConfig',
    'storages',
    'reversion',
    'geoposition',
    'rest_framework',
    'django_select2',
    'session_security',
]

AUTH_USER_MODEL = 'back_office.Employee'

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'session_security.middleware.SessionSecurityMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Acriladmin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates', ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'Acriladmin.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

if IS_RUNNING_ON_HEROKU:
    default_database = dj_database_url.config()
else:
    default_database = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

DATABASES = {
    'default': default_database,
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AdminSite.site_header = "Acriladmin - ERP"
AdminSite.site_title = "Acriladmin"

AuthConfig.verbose_name = "Autorización y autenticación"

STATIC_ROOT = 'collected_static'
MEDIA_ROOT = 'media'

if "AWS_ACCESS_KEY_ID" in os.environ and \
                "AWS_SECRET_ACCESS_KEY" in os.environ and \
                "AWS_STORAGE_BUCKET_NAME" in os.environ and \
        not DEBUG:
    # AWS S3 - Tutorial for this section at:
    # https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")

    AWS_S3_CUSTOM_DOMAIN = '{0}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)

    AWS_HEADERS = {
        'Expires': 'Thu, 15 Apr 2099 20:00:00 UTC',
        'Cache-Control': 'max-age=94608000',
    }

    STATICFILES_LOCATION = STATIC_ROOT
    STATICFILES_STORAGE = 'utils.custom_storages.StaticStorage'
    STATIC_URL = "https://{0}/{1}/".format(AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

    MEDIAFILES_LOCATION = MEDIA_ROOT
    DEFAULT_FILE_STORAGE = 'utils.custom_storages.MediaStorage'
else:
    STATIC_URL = '/{0}/'.format(STATIC_ROOT)
    MEDIA_URL = '/{0}/'.format(MEDIA_ROOT)

GEOPOSITION_MAP_OPTIONS = {
    'minZoom': 3,
    'maxZoom': 15,
}

GEOPOSITION_MARKER_OPTIONS = {
    'cursor': 'move'
}

CITIES_LIGHT_APP_NAME = 'back_office'
CITIES_LIGHT_TRANSLATION_LANGUAGES = ['es_MX']
CITIES_LIGHT_INCLUDE_COUNTRIES = ['MX', 'US']
CITIES_LIGHT_INCLUDE_CITY_TYPES = ['PPL', 'PPLA', 'PPLA2', 'PPLA3', 'PPLA4', 'PPLC', 'PPLF', 'PPLG', 'PPLL', 'PPLR',
                                   'PPLS', 'STLMT']

# Django session security
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SECURITY_WARN_AFTER = 350
SESSION_SECURITY_EXPIRE_AFTER = 420
