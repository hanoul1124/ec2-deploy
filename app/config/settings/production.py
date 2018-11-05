# for Production(Use for Deployment version)

from .base import *

DEBUG = False

WSGI_APPLICATION = 'config.wsgi.application'

production_set = json.load(open(os.path.join(SECRETS_DIR, 'production.json')))

DATABASES = production_set['DATABASES']
