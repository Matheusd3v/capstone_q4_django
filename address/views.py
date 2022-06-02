from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from address.models import Address
from rest_framework import status
from user.models import User
from rest_framework.response import Response

from address.serializers import AddressSerializer


class AddressViewSet(ModelViewSet):
    http_method_names: list[str] = ["get", "patch", "put", "delete", "head"]
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    @action(detail=False, methods=["put"])
    def user_addres(self, request, pk=None):
        user: User = request.user
        data = request.data

        serializer = AddressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        address_object = Address.objects.filter(**serializer.validated_data).first()

        if not address_object:
            address_object = Address.objects.create(**serializer.validated_data)

        address_object.save()

        user.address_id = address_object.address_uuid

        serializer = AddressSerializer(address_object)

        user.save()

        return Response(serializer.data)
