from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet

from products.models import Basket, Products
from api_cart.serializers import BasketSerializer


class BasketModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

    def get_queryset(self):
        return Basket.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        product = Products.objects.get(id=request.data['product_id'])
        cart, created = Basket.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart.quantity += 1
            cart.save()
            return Response(
                {
                    "status": status.HTTP_200_OK,
                    "data": {"message": "basket updated successfully"},
                }
            )
        else:
            return Response(
                {
                    "status": status.HTTP_201_CREATED,
                    "data": {"message": "basket created successfully"},
                }
            )

    def perform_destroy(self, instance):
        if instance.quantity > 1:
            instance.quantity -= 1
            instance.save()
        else:
            instance.delete()

    @action(detail=False, methods=["DELETE"])
    def destroy_all(self, request):
        self.queryset.delete()
        return Response({"status": status.HTTP_204_NO_CONTENT})
