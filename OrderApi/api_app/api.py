from rest_framework import routers
from . views import OrderViewset

router = routers.DefaultRouter()
router.register(r'orders', OrderViewset,basename='orders-api')