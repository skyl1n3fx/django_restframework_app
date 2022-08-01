from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'oracle': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': '127.0.0.1:1521/orcl',
        'USER': 'oracle_django',
        'PASSWORD' : 'oracle_django',
        'TEST' : {
            'USER' : 'default_test_tbls',
            'TBLSPACE' : 'default_test_tbls',
            'TBLSPACE_TMP' : 'default_test_tbls_tmp'
        }
    }
}

DATABASE_ROUTERS = [
    'database_routers.oracle_router.OracleRouter',
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# Indicamos donde serviremos nuestras imágenes
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')


STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
 