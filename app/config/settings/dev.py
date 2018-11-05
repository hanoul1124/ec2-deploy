# settings for Development

from .base import *

DEBUG = True

WSGI_APPLICATION = 'config.wsgi.application'

dev_set = json.load(open(os.path.join(SECRETS_DIR, 'dev.json')))

DATABASES = dev_set['DATABASES']

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = dev_set['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = dev_set['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = dev_set['AWS_STORAGE_BUCKET_NAME']


