# settings for Development

from .base import *

DEBUG = True

WSGI_APPLICATION = 'config.wsgi.application'

dev_set = json.load(open(os.path.join(SECRETS_DIR, 'dev.json')))

DATABASES = dev_set['DATABASES']

