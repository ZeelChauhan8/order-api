from django.urls import path
from . import views

urlpatterns=[
   path('',views.apioverview,name='api-overview'),
   path('order-list/',views.OrderList,name='order-list'),
   path('order-detail/<str:pk>',views.OrderDetail,name='order-detail'),
   path('order-create/',views.OrderCreate,name='order-create'),
   path('order-update/<str:pk>',views.OrderUpdate,name='order-update'),
   path('order-delete/<str:pk>',views.OrderDelete,name='order-delete'),
   
]