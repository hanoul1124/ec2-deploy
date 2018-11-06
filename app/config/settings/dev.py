# settings for Development

from .base import *

DEBUG = True

WSGI_APPLICATION = 'config.wsgi.application'

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



