
from rest_framework.viewsets import ModelViewSet
from brand.models import Brand

from brand.serializers import BrandSerializer


class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer