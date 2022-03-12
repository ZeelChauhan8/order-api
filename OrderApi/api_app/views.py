from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .serializer import OrderSerializer,Delayed_order_Serializer
from .models import Delayed_orders, Orders

# Create your views here.

class OrderViewset(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

class DelayedOrderViewset(viewsets.ModelViewSet):
    queryset = Delayed_orders.objects.all()
    serializer_class = Delayed_order_Serializer


# @api_view(['GET'])     # get all records 
# def DelayOrderList(request):
#     delayorder=Delayed_orders.objects.all()
#     serializer=Delayed_order_Serializer(delayorder,many=True) 
#     return Response(serializer.data)