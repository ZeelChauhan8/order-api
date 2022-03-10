from django.db import models
from viewflow.fields import CompositeKey

# Create your models here.

# Customer model 
class customers(models.Model):
    c_id=models.IntegerField(primary_key=True)
    c_name=models.CharField(max_length=50)

    def __str__(self):
        return self.c_name

# Item (Product) model 
class Items(models.Model):
    i_id=models.IntegerField(primary_key=True)
    i_name=models.CharField(max_length=50)

    def __str__(self):
        return self.i_name

# Orders model :
class Orders(models.Model):
    o_id=models.IntegerField(primary_key=True)
    etd=models.TimeField()
    d_address=models.TextField()
    b_address=models.TextField()
    c_id=models.ForeignKey(customers,related_name='cust_fk',on_delete=models.CASCADE)

    def __int__(self):
        return self.o_id

#Order Details model : 
class Order_details(models.Model):
    
    o_id=models.ForeignKey(Orders,primary_key=True,related_name='order_fk',on_delete=models.DO_NOTHING)
    i_id=models.ForeignKey(Items,related_name='item_fk',on_delete=models.DO_NOTHING)
    quantity=models.IntegerField()
    
    def __int__(self):
        return self.quantity

# # Delayed order model :
# class Delayed_order(models.Model):
#     o_id=models.ForeignKey(Orders,related_name='order_fk',on_delete=models.DO_NOTHING)
#     c_time