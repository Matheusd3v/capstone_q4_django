from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from mercado.permissions import ReadOnly

from products.models import Products

from products.serializers import ProductsSerializer, ProductsDetailSerializer


class ProductsViewSet(ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]

    queryset = Products.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ProductsDetailSerializer
        if self.action == "retrieve":
            return ProductsDetailSerializer

        return ProductsSerializer
