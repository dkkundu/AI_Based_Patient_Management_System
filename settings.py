import datetime
import os

# from heartcare.jazzmin import CONFIG
from heartcare.local_settings import (
    SECRET_KEY, TEMPLATES_DIR, STATICFILES_DIR, STATIC_DIR, MEDIA_DIR,
    LOGS_DIR, DEBUG, ENABLE_HTTPS, ALLOWED_HOSTS, INTERNAL_IPS, DB_CONFIG,
    CELERY_BROKER_URL, CELERY_RESULT_BACKEND, CELERY_CACHE_BACKEND,
    CORS_ALLOWED_ORIGINS
)
from heartcare.logging import LOGGING

PROJECT_NAME = 'Patient-Management-System'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...) -------
SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SETTINGS_DIR)
TEMPLATES_DIR = os.getenv('TEMPLATES_DIR', TEMPLATES_DIR)
STATICFILES_DIR = os.getenv('STATICFILES_DIR', STATICFILES_DIR)
STATIC_DIR = os.getenv('STATIC_DIR', STATIC_DIR)
MEDIA_DIR = os.getenv('MEDIA_DIR', MEDIA_DIR)
LOGS_DIR = os.getenv('LOGS_DIR', LOGS_DIR)

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = DEBUG

ALLOWED_HOSTS = ALLOWED_HOSTS

if ENABLE_HTTPS:  # local_settings
    USE_X_FORWARDED_HOST = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# needed for debug toolbar
INTERNAL_IPS = INTERNAL_IPS  # local_settings.py

# CORS HEADERS
CORS_ALLOWED_ORIGINS = CORS_ALLOWED_ORIGINS
CORS_ALLOW_ALL_ORIGINS = DEBUG  # Allows from all origins when DEBUG mode is on

# Application definition ------------------------------------------------------


DJANGO_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PLAGIN_APPS = [
    'widget_tweaks',
    'django_extensions',
    'debug_toolbar',
    'django_prometheus',
    'import_export',
    'crispy_forms',
    'bootstrap_datepicker_plus',
    'ckeditor',
    'ckeditor_uploader',
    'weasyprint',
    'rest_framework'

]

PROJECT_APPS = [
    'core.apps.CoreConfig',
    'hospital.apps.HospitalConfig',
    'appointment.apps.AppointmentConfig',
    'address.apps.AddressConfig',
    'patient_ms.apps.PatientMsConfig',
]

INSTALLED_APPS = DJANGO_APPS + PLAGIN_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django_prometheus.middleware.PrometheusBeforeMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django_prometheus.middleware.PrometheusAfterMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
ROOT_URLCONF = 'heartcare.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR, ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'hospital.context_processors.footer_content',
            ],
            'libraries': {
                'group_checker_tag': 'patient_ms.templatetags.group_checker_tag',

            }
        },
    },
]

WSGI_APPLICATION = 'heartcare.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'core.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

CRISPY_TEMPLATE_PACK = 'bootstrap4'

BOOTSTRAP4 = {
    'include_jquery': True,
}
STATIC_URL = '/static/'
STATIC_ROOT = STATIC_DIR
STATICFILES_DIRS = [STATICFILES_DIR, ]
MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR

# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your email'
EMAIL_HOST_PASSWORD = 'your password'

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'height': 250,
        'width': 700,
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            [
                'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
                'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'
            ],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ]
    }
}
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
