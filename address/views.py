from rest_framework.viewsets import ModelViewSet, SerializerMethodField
from rest_framework.decorators import action
from rest_framework.response import Response
from address.models import Address
from user.models import User

from address.serializers import AddressSerializer


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    http_method_names = ["get", "put", "head"]

    @action(detail=False, methods=["put"])
    def addAddressInUser(self, request, pk=None):
        user = self.request.user
        data_address = self.request.body

        return Response({"status": "ok"})


# {
#     "street": "Rua da Saudades",
#     "number": 69,
#     "city": "Bacanal",
#     "state": "No Harem",
#     "zip_code": "1200000",
#     "country": "Paraíso",
# }
