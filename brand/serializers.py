from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueTogetherValidator

from brand.models import Brand
from products.serializers import ProductsSerializer


class BrandSerializer(ModelSerializer):

    products = ProductsSerializer(required=False, many=True, read_only=True)

    class Meta:
        model = Brand
        fields = [
            "brand_uuid",
            "name",
            "site",
            "products",
        ]
        validators = [
            UniqueTogetherValidator(
                queryset=Brand.objects.all(), fields=["name", "site"]
            )
        ]
        depth = 1


# def validate(self, attrs):
#     attrs["name"] = attrs["name"].title()
#     attrs["site"] = attrs["site"].lower()

#     return super().validate(attrs)
