from django.contrib import admin
from . models import customers,Items,Orders,Order_details,Delayed_orders

# Register your models here.
admin.site.register(customers)
admin.site.register(Items)
admin.site.register(Orders)
admin.site.register(Order_details)
admin.site.register(Delayed_orders)
