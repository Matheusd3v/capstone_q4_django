from rest_framework.viewsets import ModelViewSet
from brand.models import Brand

from rest_framework.permissions import IsAdminUser
from mercado.permissions import ReadOnly

from brand.serializers import BrandSerializer


class BrandViewSet(ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
