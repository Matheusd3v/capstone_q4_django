from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from address.views import AddressViewSet
from category.views import CategoryViewSet

router = routers.DefaultRouter()

router.register(r"addresses", AddressViewSet, basename="addresses")
router.register(r"categories", CategoryViewSet, basename="categories")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
