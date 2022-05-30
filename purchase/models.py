from uuid import uuid4
from django.db import models


class Purchase(models.Model):
    class StatusPurchase(models.IntegerChoices):
        CART = 1, "Cart"
        ACCOMPLISHED = 2, "Accomplished"
        PAID = 3, "Paid"
        DELIVERED = 4, "Delivered"

    purchase_uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, related_name="purchase"
    )
    status = models.IntegerField(
        choices=StatusPurchase.choices, default=StatusPurchase.CART
    )

    def __str__(self):
        return "%s - %s" % (self.user, self.status)


class ItensPurchase(models.Model):
    items_purchase_uuid = models.UUIDField(
        primary_key=True, default=uuid4, editable=False
    )
    purchase = models.ForeignKey(
        "purchase.Purchase", on_delete=models.CASCADE, related_name="itens"
    )
    products = models.ForeignKey(
        "products.Products", on_delete=models.PROTECT, related_name="+"
    )
    quantity = models.IntegerField()
