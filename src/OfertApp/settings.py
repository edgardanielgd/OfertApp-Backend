"""
Django settings for Lab0Backend project.

Generated by 'django-admin startproject' using Django 3.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import environ
import os
from datetime import timedelta

import pymysql
pymysql.install_as_MySQLdb()

from django.db.backends.mysql.base import DatabaseWrapper
DatabaseWrapper.data_types['DateTimeField'] = 'datetime' # fix for MySQL 5.5

# Read env data
env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env( os.path.join(BASE_DIR, "./../.env") )

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG", default=False, cast=bool)

# Allow requests which doesn't end with /
APPEND_SLASH = False

# Get Backend's domain name:
WEB_URL = env("WEB_URL")

ALLOWED_HOSTS = [
    "localhost",
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.auth.hashers',
    'auth.apps.AuthConfig',
    'publications.apps.PublicationsConfig',
    'reports.apps.ReportsConfig',
    'comments.apps.CommentsConfig',
    'admins.apps.AdminsConfig',
    'util.apps.UtilConfig',
    'core.apps.CoreConfig',
    "rest_framework",
    "corsheaders",
    "django_seed"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]

# Overwrite rest_framework default settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# Overwrite JWT default settings
SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer",),
    "TOKEN_OBTAIN_SERIALIZER": "auth.token.serializers.CustomTokenPairSerializer",
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": True,
    "ALGORITHM": "HS256",
}

# Overwritting auth backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'auth.backends.CustomBackend'
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'OfertApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'OfertApp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env("DB_NAME"),
        'USER' : env("DB_USER"),
        'PASSWORD' : env("DB_PASSWORD"),
        'HOST' : env("DB_HOST"),
        'PORT' : env("DB_PORT"),
    }
}

# Overwrite default user auth model
AUTH_USER_MODEL = 'users_auth.User'

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# Password hashers
# https://docs.djangoproject.com/en/3.2/topics/auth/passwords/#using-bcrypt-with-django
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]

# Config media urls
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Smtp config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True

# Tokens default expiration time
PASSWORD_RESET_TIMEOUT = 7200 # 2 Hours

# MasterCard data
MC_API_BASE_URL= env("MC_API_BASE_URL")
MC_PRIVATE_KEY_PATH = env("MC_PRIVATE_KEY_PATH")
MC_CARD_KEY_PASSWORD = env("MC_CARD_KEY_PASSWORD")
MC_CONSUMER_KEY = env("MC_CONSUMER_KEY")

# Municipality service
MUNICIPALITY_SERVICE_URL = "https://www.datos.gov.co/resource/xdk5-pm3f.json"

# Get verification endpoint
EMAIL_VERIFICATION_URL_ENDPOINT = env("EMAIL_VERIFICATION_URL_ENDPOINT")

# Get password recovery endpoint
EMAIL_PASSWORD_RESET_URL_ENDPOINT = env("EMAIL_PASSWORD_RESET_URL_ENDPOINT")

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
