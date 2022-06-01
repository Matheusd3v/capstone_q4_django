from rest_framework.viewsets import ModelViewSet
from user.models import User
from user.permissions import CreateSuperuser
from rest_framework.authentication import TokenAuthentication

from user.serilizers import UsersSerializer


class UserViewSet(ModelViewSet):
    http_method_names = ["post", "head"]
    permission_classes = [CreateSuperuser]

    queryset = User.objects.all()
    serializer_class = UsersSerializer
