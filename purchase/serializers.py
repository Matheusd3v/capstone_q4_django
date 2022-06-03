from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from purchase.models import Purchase, ItensPurchase


class ItensPurchaseSerializer(ModelSerializer):
    total = SerializerMethodField()

    class Meta:
        model = ItensPurchase
        fields = (
            "products",
            "quantity",
            "total",
        )
        depth = 2

    def get_total(self, instance):
        return instance.quantity * instance.products.price


class PurchaseSerializer(ModelSerializer):
    user = CharField(source="user.email")
    status = SerializerMethodField()
    itens = ItensPurchaseSerializer(many=True)

    class Meta:
        model = Purchase
        fields = ("purchase_uuid", "user", "status", "itens", "total")

    def get_status(self, instance):
        return instance.get_status_display()


class CreateAndEditItensPurchaseSerializer(ModelSerializer):
    class Meta:
        model = ItensPurchase
        fields = (
            "products",
            "quantity",
        )


class CreateAndEditPurchaseSerializer(ModelSerializer):
    itens = CreateAndEditItensPurchaseSerializer(many=True)

    class Meta:
        model = Purchase
        fields = ("purchase_uuid", "user", "itens")

    def create(self, validated_data):
        itens = validated_data.pop("itens")
        purchase = Purchase.objects.create(**validated_data)
        for item in itens:
            ItensPurchase.objects.create(purchase=purchase, **item)
        purchase.save()
        return purchase
