from uuid import uuid4
from django.db import models


class Address(models.Model):
    class Meta:
        verbose_name_plural = "addresses"

    address_uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    street = models.CharField(max_length=255)
    number = models.IntegerField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return "%s-%s (%s)" % (self.city, self.state, self.country)
