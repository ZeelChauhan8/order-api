from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
import time


class Command(BaseCommand):
    help = "This Command will fetch balance of all sub-account and store them in SubAccountBalance model"

    def handle(self, *args, **kwargs):
        
        print(f'Hello !! {time}')