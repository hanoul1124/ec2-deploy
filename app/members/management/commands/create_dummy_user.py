from django.core.management.base import BaseCommand, CommandError
from members.models import *
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = "더미 유저를 생성합니다."
    def handle(self, *args, **options):
        User.objects.create(name=get_random_string(length=10))
