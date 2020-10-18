from .settings import *
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'decumx',
        'HOST': 'localhost',
        'USER': config('user'),
        'PASSWORD': config('pass'),
        'PORT': config('port'),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
             'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}


DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
STATICFILES_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
DROPBOX_OAUTH2_TOKEN = config('key')
DROPBOX_ROOT_PATH = 'static'

"""
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID') 
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')  
AWS_STORAGE_BUCKET_NAME =  config('AWS_STORAGE_BUCKET_NAME') 
AWS_DEFAULT_ACL = None
AWS_S3_FILE_OVERWRITE = config('AWS_S3_FILE_OVERWRITE', cast=bool)
AWS_QUERYSTRING_AUTH = config('AWS_QUERYSTRING_AUTH', cast=bool) 
DEFAULT_FILE_STORAGE =  config('DEFAULT_FILE_STORAGE') 
STATICFILES_STORAGE =  config('STATICFILES_STORAGE') 
AWS_S3_HOST = config('AWS_S3_HOST') 
AWS_S3_REGION_NAME = config('AWS_S3_REGION_NAME') 


AWS_S3_CUSTOM_DOMAIN='%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
"""

django_heroku.settings(locals(), staticfiles=False)