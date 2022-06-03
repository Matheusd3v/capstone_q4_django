from rest_framework.viewsets import ModelViewSet
from category.models import Category

from category.serializers import CategorySerializer

from rest_framework.permissions import IsAdminUser
from mercado.permissions import ReadOnly


class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
