from django.urls import path
from .views import OrderViewset,DelayedOrderViewset
from rest_framework.routers import DefaultRouter
from . import views
  

router = DefaultRouter()
router.register('', OrderViewset, basename='order-api')
router.register('delayed', DelayedOrderViewset, basename='delayed-order')



urlpatterns = router.urls
 

   