from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    # 이 Storage를 사용해서 저장되는 파일들이 <location>값/<추가 경로> 부분에 저장된다.
    location = 'media'
    default_acl = 'private'

# class StaticStorage(S3Boto3Storage):
#     location = 'static'
#     default_acl = 'public-read'
# ACL > AWS S3 에 대한 접근권한 설정
