from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from address.views import AddressViewSet
from brand.views import BrandViewSet
from category.views import CategoryViewSet
from products.views import ProductsViewSet
from purchase.views import PurchaseViewSet

router = routers.DefaultRouter()

router.register(r"addresses", AddressViewSet, basename="addresses")
router.register(r"brands", BrandViewSet, basename="brands")
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"products", ProductsViewSet, basename="products")
router.register(r"purchases", PurchaseViewSet, basename="purchases")
router.register(r"users", PurchaseViewSet, basename="users")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("", include(router.urls)),
]
