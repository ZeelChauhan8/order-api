from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import OrderSerializer
from .models import Orders

# Create your views here.

#api_overview view
@api_view(['GET'])
def apioverview(request):
    api_urls={
        'API overview' :'orders/v1',
        'List':'order-list/',
        'Details View':'order-list/<str:pk>/',
        'Create':'order-create',
        'Update':'order-update/<str:pk>/',
        'Delete':'order-delete/<str:pk>/',
    }
    return Response(api_urls)

#List order details view
@api_view(['GET'])
def OrderList(request):
    order=Orders.objects.all()
    serializer=OrderSerializer(order,many=True)
    return Response(serializer.data)

#List order details by perticular id 
@api_view(['GET'])
def OrderDetail(request,pk):
    order=Orders.objects.get(o_id=pk)
    serializer=OrderSerializer(order,many=False)
    return Response(serializer.data)

#Create order details view
@api_view(['POST'])
def OrderCreate(request):
    serializer=OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#Update order details view 
@api_view(['PATCH'])
def OrderUpdate(request,pk):
    order=Orders.objects.get(o_id=pk)
    serializer=OrderSerializer(instance=order,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#Delete order details by o_id view
@api_view(['DELETE'])
def OrderDelete(request,pk):
    order=Orders.objects.get(o_id=pk)
    order.delete()
    return Response('Order details deleted successfully !! ')


