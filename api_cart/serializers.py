from rest_framework import serializers
from products.models import Products, Basket, Categories


class ProductsSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', queryset=Categories.objects.all())

    class Meta:
        model = Products
        fields = ('id', 'name', 'description', 'price', 'image', 'category',)


class BasketSerializer(serializers.ModelSerializer):
    product = ProductsSerializer()

    class Meta:
        model = Basket
        fields = ('id', 'user', 'product', 'quantity',)
