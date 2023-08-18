from django.urls import include, path
from rest_framework import routers

from api_products.views import ProductsModelViewSet

router = routers.DefaultRouter()
router.register("", ProductsModelViewSet, basename="products")

urlpatterns = [
    path("", include(router.urls)),
]
