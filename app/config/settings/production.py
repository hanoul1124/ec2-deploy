# for Production(Use for Deployment version)

from .base import *

DEBUG = False
ALLOWED_HOSTS = ['abc']

WSGI_APPLICATION = 'config.wsgi.production.application'

production_set = json.load(open(os.path.join(SECRETS_DIR, 'production.json')))

DATABASES = production_set['DATABASES']

DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
# STATICFILES_STORAGE = 'config.storages.StaticStorage'
AWS_ACCESS_KEY_ID = production_set['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = production_set['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = production_set['AWS_STORAGE_BUCKET_NAME']

# 지역 설정

# 로그폴더 생성
LOG_DIR = os.path.join(ROOT_DIR, '.log')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR, exist_ok=True)

LOGGING = {
    'version': 1,
    'formatters': {
        'default':{
            'format':'[%(levelname)s] %(name)s (%(asctime)s)\n\t%(message)s'
        },
    },
    'handlers': {
        'file_error': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'filename': os.path.join(LOG_DIR, 'error.log'),
            'formatter': 'default',
            'maxBytes': 1048576,
            'backupCount': 10,
        },
        'file_info':{

        },
        'console': {
            'class' : 'logging.StreamHandler',
            'level': 'INFO',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file_error', 'console'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}

