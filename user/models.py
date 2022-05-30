from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    address = models.ForeignKey(
        "address.Address", on_delete=models.RESTRICT, related_name="users", null=True
    )

    def __str__(self):
        return "%s - %s" % (self.username, self.address)
