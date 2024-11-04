"""
Django settings for nnlms project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os 
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=ihep)-gjq@b1ynk1c546imffs$jwld&8l99iib2)fwowjfbgp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.getenv("debug"))


ALLOWED_HOSTS = ['192.168.8.112','nn4m.herokuapp.com', 'localhost', 'test-server134.herokuapp.com', 'lms.99formed.com', '127.0.0.1', 'temp-6249858623c0.herokuapp.com']

CSRF_FAILURE_VIEW = 'general.views.csrf_failure'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_better_admin_arrayfield',
    'general',
    'Tutors',
    'Forum',
    'storages',
    'interview', 
    'channels',
    'live_class'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'general.middleware.ZoomTokenMiddleware',
    # 'Tutors.middleware.TutorsZoomTokenMiddleware'
]

ROOT_URLCONF = 'nnlms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['general/templates/', 'authentication/templates/', 'interview/templates/'],
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

ASGI_APPLICATION = 'nnlms.asgi.application'
WSGI_APPLICATION = 'nnlms.wsgi.application'



# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.getenv('CURRENT_DB_ENGINE'),
        'NAME': os.getenv('CURRENT_DB_NAME'),
        'USER': os.getenv('CURRENT_DB_USER'),
        'PASSWORD': os.getenv('CURRENT_DB_PASSWORD'),
        'HOST': os.getenv('CURRENT_DB_HOST'),
        'PORT': os.getenv('CURRENT_DB_PORT'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
    '/var/www/static/',
]


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'







STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/') 

# if os.getenv("localhost"):
#     SECURE_SSL_REDIRECT = False
# else:
#     SECURE_SSL_REDIRECT = True

if os.getenv("localhost"):
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# This supposedly tells django that the incoming HTTPS request is from a trusted origin
# Let's see if it works
# 
CSRF_TRUSTED_ORIGINS = ['https://lms.99formed.com']
# if not DEBUG:
#     AWS_ACCESS_KEY_ID = os.getenv('BUCKETEER_AWS_ACCESS_KEY_ID')
#     AWS_SECRET_ACCESS_KEY = os.getenv('BUCKETEER_AWS_SECRET_ACCESS_KEY')
#     AWS_STORAGE_BUCKET_NAME = os.getenv('BUCKETEER_BUCKET_NAME')
#     AWS_S3_REGION_NAME = os.getenv('BUCKETEER_AWS_REGION')
#     AWS_S3_FILE_OVERWRITE = False
#     AWS_DEFAULT_ACL = None
#     DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

if DEBUG == False:
    import mimetypes
    mimetypes.add_type("text/css", ".css", True)
    mimetypes.add_type("text/html", ".css", True)
    mimetypes.add_type("text/html", ".html", True)
