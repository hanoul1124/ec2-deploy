# for Production(Use for Deployment version)

from .base import *

DEBUG = False

WSGI_APPLICATION = 'config.wsgi.application'

secrets = json.load(open(os.path.join(SECRETS_DIR, 'production.json')))

DATABASES = secrets['DATABASES']
