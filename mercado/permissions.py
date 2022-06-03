from rest_framework.permissions import BasePermission
from rest_framework.exceptions import NotAuthenticated
from rest_framework.views import Request

from user.models import User

SAFE_METHODS = ["GET", "HEAD", "OPTIONS"]


class CreateSuperuser(BasePermission):
    def has_permission(self, request: Request, _):
        user: User = request.user
        is_superuser: bool = request.data.get("is_superuser", False)

        if is_superuser and (not user.is_authenticated or not user.is_superuser):
            raise NotAuthenticated("Only admin can create a superuser.")

        return True


class ReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):

        if request.method in SAFE_METHODS and request.user.is_authenticated:
            return True
        return False
