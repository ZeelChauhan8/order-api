from re import L
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from ...models import Orders
from rest_framework.decorators import api_view
from ...serializer import OrderSerializer,Delayed_order_Serializer
from rest_framework.response import Response
import time
from datetime import datetime
now = datetime.now()


class Command(BaseCommand):
    help = "This Command will insert record if current time > expected time of delivery else not "

    def handle(self, *args, **kwargs):
        current_time = now.strftime("%H:%M:%S")
        order=Orders.objects.values('etd')
        for etd in order:
            if current_time > str(etd):
                serializer=Delayed_order_Serializer(data={"current_time":current_time,"etd":str(etd),"order_id":"1"})
                if serializer.is_valid(): 
                    serializer.save() 
                print(Response(serializer.data))
        

