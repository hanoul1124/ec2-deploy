# for Production(Use for Deployment version)

from .base import *

DEBUG = False

WSGI_APPLICATION = 'config.wsgi.production.application'

production_set = json.load(open(os.path.join(SECRETS_DIR, 'production.json')))

DATABASES = production_set['DATABASES']

DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
STATICFILES_STORAGE = 'config.storages.StaticStorage'
AWS_ACCESS_KEY_ID = production_set['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = production_set['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = production_set['AWS_STORAGE_BUCKET_NAME']