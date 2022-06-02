from rest_framework.viewsets import ModelViewSet
from user.models import User
from user.permissions import CreateSuperuser
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import Response

from user.serializers import UsersSerializer


class UserViewSet(ModelViewSet):
    http_method_names = ["get", "post", "head"]
    permission_classes = [CreateSuperuser]

    queryset = User.objects.all()
    serializer_class = UsersSerializer

    def get_queryset(self):

        if self.request.user.is_anonymous:
            raise AuthenticationFailed("Missing authorization token.")

        user = self.request.user

        if user.is_superuser:
            return User.objects.all()

        return User.objects.filter(user_uuid=user.user_uuid)
