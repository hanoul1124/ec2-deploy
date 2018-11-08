import logging

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
# from members.models import *
User = get_user_model()
from django.utils.crypto import get_random_string

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "더미 유저를 생성합니다."
    def handle(self, *args, **options):
        username=f'dummy_{get_random_string(length=10)}'
        User.objects.create_user(username=username)
        self.stdout.write(f'User {username} created')
