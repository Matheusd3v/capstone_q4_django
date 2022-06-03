from rest_framework.viewsets import ModelViewSet
from purchase.models import Purchase

from purchase.serializers import PurchaseSerializer, CreateAndEditPurchaseSerializer


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    # serializer_class = PurchaseSerializer

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return PurchaseSerializer
        return CreateAndEditPurchaseSerializer
