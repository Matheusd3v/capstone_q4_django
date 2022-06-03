from uuid import uuid4
from django.db import models


class Products(models.Model):
    class Meta:
        verbose_name_plural = "products"

    products_uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=60)
    price = models.FloatField()
    quantity = models.IntegerField()

    brand = models.ForeignKey(
        "brand.Brand", on_delete=models.PROTECT, related_name="products"
    )
    category = models.ForeignKey(
        "category.Category", on_delete=models.PROTECT, related_name="products"
    )

    def __str__(self):
        return "%s (%s - %s)" % (self.name, self.brand.name, self.brand.site)
