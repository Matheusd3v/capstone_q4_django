from rest_framework.serializers import ModelSerializer

from purchase.models import Purchase


class PurchaseSerializer(ModelSerializer):
    class Meta:
        model = Purchase
        fields = "__all__"
