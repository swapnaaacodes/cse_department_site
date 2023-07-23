"""
Django settings for cse_department_site project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

from decouple import config

import platform

DJANGO_SECRET_KEY = config('DJANGO_SECRET_KEY')

if platform.system() != 'Windows':
    NPM_BIN_PATH = '/usr/bin/npm'
else:
    # Handle other platforms if needed
    NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Templates Directory
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

TAILWIND_APP_NAME = 'theme'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = DJANGO_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'csedepartmentsite-production.up.railway.app',
                 'https://csedepartmentsite-production.up.railway.app/', 'https://cse-department-site-6uh9fi1si-000jd.vercel.app/', 'cse-department-site-6uh9fi1si-000jd.vercel.app']

CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"

CRISPY_TEMPLATE_PACK = "tailwind"

CSRF_TRUSTED_ORIGINS = ['https://csedepartmentsite-production.up.railway.app',
                        'https://www.csedepartmentsite-production.up.railway.app',
                        'https://cse-department-site-6uh9fi1si-000jd.vercel.app/']
# Application definition

INSTALLED_APPS = [

    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'base',
    'accounts',
    'about',
    'events',

    'tailwind',
    'theme',
    "crispy_forms",
    "crispy_tailwind",
    'django_browser_reload',
    'whitenoise.runserver_nostatic',
]

INTERNAL_IPS = [
    "127.0.0.1",
]

JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",
    "dark_mode_theme": "solar",
}

JAZZMIN_SETTINGS = {
    "site_header": "CSE DEPARTMENT",
    "site_brand": "CSE DEPARTMENT",
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    "django_browser_reload.middleware.BrowserReloadMiddleware",

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = 'cse_department_site.urls'

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'cse_department_site.wsgi.application'

AUTH_USER_MODEL = 'accounts.Users'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators


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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

TAILWIND_CSS_PATH = 'css/dist/styles.css'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "thems/static/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'thems/static/images')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'thems/static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
