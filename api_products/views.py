from rest_framework.viewsets import ModelViewSet

from api_products.permissions import IsStaffOrReadOnly
from api_products.serializers import ProductsSerializer
from products.models import Products


class ProductsModelViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [IsStaffOrReadOnly]
