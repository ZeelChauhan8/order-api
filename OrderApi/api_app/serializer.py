from rest_framework import serializers
from . models import Orders,Delayed_orders

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields='__all__'
        
class Delayed_order_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Delayed_orders
        fields='__all__'
    
