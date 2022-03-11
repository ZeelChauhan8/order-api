from django.urls import path
from .views import OrderViewset
from rest_framework.routers import DefaultRouter
   
   # path('orders/v1',views.OrderDetail,name='order-detail'),
   # path('order-create/',views.OrderCreate,name='order-create'),
   # path('order-update/<str:pk>',views.OrderUpdate,name='order-update'),
   # path('order-delete/<str:pk>',views.OrderDelete,name='order-delete'),

router = DefaultRouter()
router.register('', OrderViewset, basename='order-api')
urlpatterns = router.urls
   