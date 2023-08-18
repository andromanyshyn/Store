from rest_framework import serializers

from products.models import Categories, Products


class ProductsSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field="name", queryset=Categories.objects.all()
    )

    class Meta:
        model = Products
        fields = (
            "id",
            "name",
            "description",
            "price",
            "image",
            "category",
        )
