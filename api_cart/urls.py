from django.urls import include, path
from rest_framework import routers

from api_cart.views import BasketModelViewSet

router = routers.DefaultRouter()
router.register("", BasketModelViewSet, basename="carts")

urlpatterns = [
    path("", include(router.urls)),
]
