# settings for Development

from .base import *

DEBUG = True

WSGI_APPLICATION = 'config.wsgi.dev.application'

dev_set = json.load(open(os.path.join(SECRETS_DIR, 'dev.json')))

DATABASES = dev_set['DATABASES']

# Django-storages
# ~/.aws/credentials
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'

# collectstatic을 실행했을 때,
# 버킷의 'static'폴더 아래에 정적파일들이 저장되도록 설정해보기
#  config.storages.StaticStorage클래스를 만들어서 적용

# STATICFILES_STORAGE = 'config.storages.StaticStorage'
# 위 설정 시 S# 프리티어 기본 PUT한계를 금방 초과하므로 STATIC_ROOT에 collectstatic한 후
# Nginx에서 제공하는 방식으로(기존 방식으로)

AWS_ACCESS_KEY_ID = dev_set['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = dev_set['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = dev_set['AWS_STORAGE_BUCKET_NAME']

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



