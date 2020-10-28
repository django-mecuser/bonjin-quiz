"""
Django settings for bonjin_quiz project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import dj_database_url
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'question.apps.QuestionConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #ホワイトノイズ本番環境での静的ファイルの提供をサポート
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'bonjin_quiz.urls'

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

WSGI_APPLICATION = 'bonjin_quiz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}


#DATABASES = {
#    'default':{
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'quize_user',
#        'USER': 'postgres',
#        'PASSWORD': 'mecmecmec',
#        'HOST': '127.0.0.1',
#        'PORT': '5432',
#    }
#}

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dd8g7h70omceog',
        'USER': 'phvhozisfnxjjh',
        'PASSWORD': 'ff4cc461703980bdd1f20271a9e0e86bb200f39bf0b98a8130da03eab110593b',
        'HOST': 'ec2-34-231-56-78.compute-1.amazonaws.com',
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

#ローカルセッティングをインポート
try:
    from .local_settings import *
except ImportError:
    pass

#本番環境時の設定
if not DEBUG:
    #秘密鍵の設定
    SECRET_KEY = os.environ['SECRET_KEY']
    #django_herokuの設定
    import django_heroku 
    django_heroku.settings(locals())

#公式ドキュメントより、DATABASE_URL環境変数の値が解析され、Djangoが理解できるものに変換されます。Djangoとpsqlの接続
db_from_env = dj_database_url.config(conn_max_age=600,ssl_require=True)
DATABASES['default'].update(db_from_env)

#cssの設定
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


