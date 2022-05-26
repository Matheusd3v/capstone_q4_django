from django.urls import path, include
from django.contrib import admin
from User.views import UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
]
