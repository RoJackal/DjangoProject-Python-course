"""
Django settings for DjangoProject project.
Optimized for Django 6.0 & Python 3.14
"""

import os
from pathlib import Path
from dotenv import load_dotenv
# 1. PATHS & ENV
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

# 2. CORE SECURITY
# Folosim o valoare default doar pentru dev, dar .env va suprascrie asta
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-fallback-key-replace-me')

DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')

# 3. APP DEFINITION
INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	# Third-party
	'django_extensions',
	'whitenoise.runserver_nostatic',  # Recomandat pentru WhiteNoise
	# Local Apps
	'intro',
	'home',
	'employee',
	'manager',
	'userextend',
	]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'whitenoise.middleware.WhiteNoiseMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	]

ROOT_URLCONF = 'DjangoProject.urls'

TEMPLATES = [
	{
		'BACKEND':  'django.template.backends.django.DjangoTemplates',
		'DIRS':     [BASE_DIR / 'templates'],
		'APP_DIRS': True,
		'OPTIONS':  {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				'DjangoProject.context_processors.get_all_employees',
				],
			},
		},
	]

WSGI_APPLICATION = 'DjangoProject.wsgi.application'

# 4. DATABASE
DATABASES = {
	'default': {
		'ENGINE':  'django.db.backends.sqlite3',
		'NAME':    BASE_DIR / 'db.sqlite3',
		'OPTIONS': {
			'timeout': 20,
			}
		}
	}

# 5. AUTH & PASSWORDS
AUTH_PASSWORD_VALIDATORS = [
	{ 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator' },
	{ 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS': { 'min_length': 8 } },
	{ 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator' },
	{ 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator' },
	]

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'

# 6. INTERNATIONALIZATION
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Bucharest'
USE_I18N = True
USE_TZ = True

# 7. STATIC & MEDIA FILES
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# WhiteNoise optimization
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 8. EMAIL CONFIGURATION
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', '587'))
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', EMAIL_HOST_USER)
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_TIMEOUT = 10

# 9. DEPLOYMENT SECURITY (W004, W008, W012, W016)
if not DEBUG:
	SECURE_SSL_REDIRECT = os.getenv('SECURE_SSL_REDIRECT', 'True') == 'True'
	SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE', 'True') == 'True'
	CSRF_COOKIE_SECURE = os.getenv('CSRF_COOKIE_SECURE', 'True') == 'True'
	
	# HSTS settings
	SECURE_HSTS_SECONDS = 31536000  # 1 an
	SECURE_HSTS_INCLUDE_SUBDOMAINS = True
	SECURE_HSTS_PRELOAD = True
else:
	# Setări explicite pentru local dev pe Windows
	SECURE_SSL_REDIRECT = False
	SESSION_COOKIE_SECURE = False
	CSRF_COOKIE_SECURE = False

# 10. LOGGING
LOGGING = {
	'version':                  1,
	'disable_existing_loggers': False,
	'formatters':               {
		'verbose': { 'format': '{levelname} {asctime} {module} {message}', 'style': '{' },
		'simple':  { 'format': '{levelname} {message}', 'style': '{' },
		},
	'handlers':                 {
		'console': { 'level': 'INFO', 'class': 'logging.StreamHandler', 'formatter': 'simple' },
		'file':    {
			'level':     'ERROR',
			'class':     'logging.FileHandler',
			'filename':  BASE_DIR / 'django_errors.log',
			'formatter': 'verbose'
			},
		},
	'loggers':                  {
		'django':     { 'handlers': ['console', 'file'], 'level': 'INFO', 'propagate': False },
		'employee':   { 'handlers': ['console', 'file'], 'level': 'DEBUG', 'propagate': False },
		'userextend': { 'handlers': ['console', 'file'], 'level': 'DEBUG', 'propagate': False },
		},
	}

# Security Settings for SSL
SECURE_SSL_REDIRECT = False  # Set to True only if you want to force HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
