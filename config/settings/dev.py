"""
Django settings for snippod boilerplate project.

This is a base starter for snippod.

For more information on this file, see
https://github.com/shalomeir/snippod-boilerplate

"""
from config.settings.common import *
# from config.settings.config_dev import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$6(x*g_2g9l_*g8peb-@anl5^*8q!1w)k&e&2!i)t6$s8kia93'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', True)

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS += (
    'debug_toolbar',
)

# MIDDLEWARE_CLASSES += (
# )


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


# Database (SQLITE3 CONFIG)
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
# DATABASE_OPTIONS = {'charset': 'utf8'}

##############################################################################

# Database (POSTGRESQL CONFIG)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'asanni_db',
        'USER': 'sergioruizdavila',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

# TODO: Comment this block when you will work locally
import dj_database_url

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'] = dj_database_url.config()

###############################################################################

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

#Do not use static server
#
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'snippod_webapp/.tmp'), # grunt serve
#     os.path.join(BASE_DIR, 'snippod_webapp/dist/client'), #grunt
#     # os.path.join(BASE_DIR, 'static'),
# )
#
# COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', False)

#MEDIA FILE (user uploaded files)

# TEMPLATE_DIRS = (
#     os.path.join(BASE_DIR, 'djangoapps/templates'),
# )
