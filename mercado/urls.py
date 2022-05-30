from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from category.views import CategoryViewSet
from brand.views import BrandViewSet

router = routers.DefaultRouter()

router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"brands", BrandViewSet, basename="brands")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
