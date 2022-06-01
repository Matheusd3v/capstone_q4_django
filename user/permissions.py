from rest_framework.permissions import BasePermission
from rest_framework.exceptions import NotAuthenticated
from rest_framework.views import Request

from user.models import User


class CreateSuperuser(BasePermission):
    def has_permission(self, request: Request, _):
        user: User = request.user
        is_superuser: bool = request.data.get("is_superuser", False)

        if is_superuser and (not user.is_authenticated or not user.is_superuser):
            raise NotAuthenticated("Only admin can create a superuser.")

        return True
