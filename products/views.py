from rest_framework.viewsets import ModelViewSet
from products.models import Products

from products.serializers import ProductsSerializer


class ProductsViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
