"""
Django settings for wisdom project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import dotenv
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Load config file
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/


# Update secret key and debug mode
SYSTEM_ENV = os.environ["SYSTEM_ENV"]

if SYSTEM_ENV == "production" or SYSTEM_ENV == "development":
    SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = os.environ['DEBUG']

elif SYSTEM_ENV == "cicd":
    DEBUG = True
    SECRET_KEY = "CICD_KEY"

else:
    KeyError("SYSTEM_ENV variable is not set or set to an unacceptable value")

if SYSTEM_ENV == "production" or SYSTEM_ENV == "development":
    SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = os.environ['DEBUG']

elif SYSTEM_ENV == "cicd":
    DEBUG = True
    SECRET_KEY = "CICD_KEY"

else:
    KeyError("SYSTEM_ENV variable is not set or set to an unacceptable value")

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'registration',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'auditory',
    'anymail',
    'widget_tweaks',
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

ROOT_URLCONF = 'wisdom.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'wisdom.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

if SYSTEM_ENV == "production" or SYSTEM_ENV == "development":
    DATABASES = {
        'default': dj_database_url.config(conn_max_age=600),
    }

elif SYSTEM_ENV == 'cicd':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Audio file storage
if SYSTEM_ENV == "production":
    # Cloud storage
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
    AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
    AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]
    AWS_S3_REGION_NAME = os.environ["AWS_S3_REGION_NAME"]
    AWS_DEFAULT_ACL = os.environ["AWS_DEFAULT_ACL"]

elif SYSTEM_ENV == "development" or SYSTEM_ENV == "cicd":
    # Local storage
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Audio file limitation
ALLOWED_AUDIO_EXTENSIONS = [
    "mp3",
    "wav",
    "wma",
    "ogg",
    "oga",
    "mogg",
]

MAX_UPLOAD_SIZE = 10485760  # 10MB

# User registration
AUTH_USER_MODEL = 'registration.User'

LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/login/"

# Email
ANYMAIL = {
    "MAILGUN_API_KEY": os.environ["MAILGUN_API"],
    "MAILGUN_SENDER_DOMAIN": os.environ["MAILGUN_DOMAIN"]
}
EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
DEFAULT_FROM_EMAIL = "example@test.com"
SERVER_EMAIL = "server@test.com"

SIGNUP_EMAIL_SUBJECT = "Wisdom: user account confirmation"
SIGNUP_MESSAGE_TEMPLATE = """
Thank you for signing up for Wisdom!
Please click the link below to activate your account :)

"""

FRONTEND_URL = "http://"
