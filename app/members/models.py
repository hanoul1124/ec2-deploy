from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    # admin에서 이 필드를 수정할 수 있도록 설정
    # members/admin.py
    # ec2-deploy/.media/user 폴더에 업로드한 파일이 저장되도록 설정
    # MEDIA_ROOT, MEDIA_URL
    img_profile = models.ImageField(upload_to='user', blank=True)
    nickname = models.CharField(max_length=20, unique=True, blank=True, null=True)