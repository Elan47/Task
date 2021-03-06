"""
Django settings for coleman project.

Generated by 'django-admin startproject' using Django.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f*)$)fay97180m+ti%xi8si##u__h(8%(ipr1z-*lsjbucooz&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = [ '*' ]


# Application definition

INSTALLED_APPS = [
    'mtasks.apps.MtasksConfig',
    'partner.apps.PartnerConfig',
    'advanced_filters',
    'django_admin_listfilter_dropdown',
    'adminfilters',
    'admin_interface',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'rest_framework',      # Uncomment this to enable the API
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'coleman.urls'

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

WSGI_APPLICATION = 'coleman.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

#
# Database config is passed in environment variable DATABASE_URL
# as string connection like postgresql://dcoleman:postgres@localhost/dcoleman_dev,
# otherwise the default SQLite database below is used.
# See more options at https://github.com/kennethreitz/dj-database-url
#
DATABASES = {
    'default': dj_database_url.config(
                    default='sqlite:///%s/db.sqlite3' % BASE_DIR,
                    conn_max_age=300)
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/


LANGUAGE_CODE = os.getenv('LANGUAGE_CODE', 'en-us')

TIME_ZONE = 'Asia/Kolkata'
# TIME_ZONE = os.getenv('TIME_ZONE', 'UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR + '/static/'


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/1.8/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            #'format': '%(levelname)s %(asctime)s [%(name)s] %(process)d %(thread)d %(message)s',
            'format': '%(asctime)s %(levelname)s [%(name)s] %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR + "/app.log",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'verbose',
        },
        # 'mail_admins': {
        #     'level': 'ERROR',
        #     'class': 'django.utils.log.AdminEmailHandler'
        # }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console', 'logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django': {
            'handlers': ['console', 'logfile'],
            'propagate': True,
            'level': 'INFO',
        },
        '': {
            'handlers': ['console', 'logfile'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    }
}


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}


#
# Custom configurations
#

APP_NAME = os.getenv('APP_NAME', 'Tuskmelon')
APP_EMAIL = os.getenv('APP_EMAIL', 'no-reply@localhost')
SITE_HEADER = os.getenv('SITE_HEADER', 'Tuskmelon Manager')

ADMINS = (
    (APP_NAME, APP_EMAIL)
)

from . settings_emails import *
