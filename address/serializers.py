from rest_framework.serializers import ModelSerializer
from user.serializers import UsersDetailsSerializer
from address.models import Address


class AddressSerializer(ModelSerializer):
    users = UsersDetailsSerializer(required=False, many=True, read_only=True)

    class Meta:
        model = Address
        fields = [
            "address_uuid",
            "street",
            "number",
            "city",
            "state",
            "zip_code",
            "country",
            "users",
        ]
        depth = 1
