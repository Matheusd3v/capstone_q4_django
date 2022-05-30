from rest_framework.viewsets import ModelViewSet
from address.models import Address

from address.serializers import AddressSerializer


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get_queryset(self):
        usuario = self.request.user

        if usuario.groups.filter(name="Administradores"):
            return Address.objects.all()
        return Address.objects.filter(usuario=usuario)
