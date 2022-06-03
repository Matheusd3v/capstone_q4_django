from rest_framework.viewsets import ModelViewSet
from purchase.models import Purchase

from purchase.serializers import PurchaseSerializer, CreateAndEditPurchaseSerializer


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return PurchaseSerializer
        return CreateAndEditPurchaseSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return Purchase.objects.all()
        return Purchase.objects.filter(user=user)
