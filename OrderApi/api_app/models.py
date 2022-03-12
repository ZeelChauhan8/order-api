from django.db import models

# Create your models here.

# Customer model 
class customers(models.Model):
    # id=models.IntegerField(primary_key=True)
    c_name=models.CharField(max_length=50)

    def __str__(self):
        return self.c_name

# Item (Product) model 
class Items(models.Model):
    # id=models.IntegerField(primary_key=True)
    i_name=models.CharField(max_length=50)

    def __str__(self):
        return self.i_name

# Orders model :
class Orders(models.Model):
    # id=models.IntegerField(primary_key=True)
    etd=models.TimeField()
    d_address=models.TextField()
    b_address=models.TextField()
    customer_id=models.ForeignKey(customers,related_name='cust_fk',on_delete=models.CASCADE)

    def __int__(self):
        return self.id

#Order Details model : 
class Order_details(models.Model):
    # id=models.IntegerField(primary_key=True)
    order_id=models.ForeignKey(Orders,related_name='order_fk',on_delete=models.DO_NOTHING)
    item_id=models.ForeignKey(Items,related_name='item_fk',on_delete=models.DO_NOTHING)
    quantity=models.IntegerField()
    
    def __int__(self):
        return self.id

# Delayed order model :
class Delayed_orders(models.Model):
    # id=models.IntegerField(primary_key=True)
    order_id=models.ForeignKey(Orders,related_name='orders_fk',on_delete=models.DO_NOTHING)
    current_time=models.TimeField()
    etd=models.TimeField()
    
    def __int__(self):
        return self.id