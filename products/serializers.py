from attr import field
from django.forms import CharField
from rest_framework.serializers import ModelSerializer, CharField
from brand.models import Brand

from products.models import Products


class BrandInProductsSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            "name",
            "site",
        )


class ProductsDetailSerializer(ModelSerializer):
    category = CharField(source="category.name")
    brand = BrandInProductsSerializer()

    class Meta:
        model = Products
        fields = (
            "products_uuid",
            "name",
            "price",
            "quantity",
            "brand",
            "category",
        )
        depth = 1


class ProductsSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"
