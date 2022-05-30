from rest_framework.viewsets import ModelViewSet
from user.models import User

from user.serilizers import UsersSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
