from django.db import models


from uuid import uuid4


class Brand(models.Model):
    class Meta:
        verbose_name_plural = "brands"

    brand_uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    site = models.CharField(max_length=255, null=True)

    def __str__(self):
        return "%s (%s)" % (self.name, self.site)