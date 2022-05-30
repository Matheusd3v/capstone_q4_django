from django.db import models

from uuid import uuid4


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    category_uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    describe = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
