from .settings import *
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'decumy',
        'HOST': 'localhost',
        'USER': config('user'),
        'PASSWORD': config('pass'),
        'PORT': config('port'),
    }
}

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

django_heroku.settings(locals())