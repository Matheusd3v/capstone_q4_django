from rest_framework.serializers import ModelSerializer

from category.models import Category
from products.serializers import ProductsSerializer


class CategorySerializer(ModelSerializer):
    products = ProductsSerializer(required=False, many=True, read_only=True)

    class Meta:
        model = Category
        fields = [
            "category_uuid",
            "name",
            "describe",
            "products",
        ]
        depth = 1

    def validate(self, attrs):
        attrs["name"] = attrs["name"].title()

        return super().validate(attrs)
