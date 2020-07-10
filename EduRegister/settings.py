"""
Django settings for EduRegister project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q9maqx2g#lr=gg3wyw0k2boe_m8$l@eep*vtq(p362xuj=vqr7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'corsheaders',       # 引入django-cors-headers解决跨域
    'rbac',
    'crm'
]

MIDDLEWARE = [
    # 'utils.cors.CORSMiddleware',
    'corsheaders.middleware.CorsMiddleware',         # 跨域添加到中间件
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS跨域设置
CORS_ORIGIN_ALLOW_ALL = True    # 全允许

ROOT_URLCONF = 'EduRegister.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'EduRegister.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'hqs2212586',
        'NAME': 'eduRegister',
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

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Django继承AbstractUser新建User,需要在setting中重载AUTH_USER_MODEL
AUTH_USER_MODEL = 'rbac.UserProfile'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'


# Media配置
MEDIA_URL = "media/"      # 静态资源路径
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

REST_FRAMEWORK = {
    # "DEFAULT_AUTHENTICATION_CLASSES": ["utils.my_auth.LoginAuth"],    # 全局视图认证
    # "ALLOWED_VERSIONS": ["v1", "v2"],  # 允许的版本
    # "VERSION_PARAM": "version",        # 版本使用的参数名称
    # "DEFAULT_VERSION": "v1",           # 默认使用的版本
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',    # 全局jwt
        'rest_framework.authentication.BasicAuthentication',        # username和password形式认证
        'rest_framework.authentication.SessionAuthentication',      #
    ),
    # 自定义异常处理
    'EXCEPTION_HANDLER': 'utils.custom.crm_exception_handler'
}

# jwt 设置
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),             # token过期时间是7天
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}

# redis设置
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = None

# 日志
BASE_LOG_DIR = os.path.join(BASE_DIR, 'logs')

LOGGING = {
'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s][%(levelname)s]''[%(filename)s:%(lineno)d][%(message)s]'
        },
        'simple': {
            'format': '[%(levelname)s][%(asctime)s]%(message)s'
        },

    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_LOG_DIR, "info_sys.log"),
            'maxBytes': 1024 * 1024 * 50,
            'backupCount': 3,
            'formatter': 'simple',
            'encoding': 'utf-8',
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_LOG_DIR, "err_sys.log"),
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',
        }

    },
    'loggers': {
        'info': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True,
        },
        'warn':{
            'handlers': ['default'],
            'level': 'WARNING',
            'propagate': True,
        },
        'error': {
            'handlers': ['error'],
            'level': 'ERROR',
        }
    }
}