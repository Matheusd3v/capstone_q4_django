from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
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
from user.views import UserViewSet

router = routers.DefaultRouter()

router.register(r"addresses", AddressViewSet, basename="addresses")
router.register(r"brands", BrandViewSet, basename="brands")
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"products", ProductsViewSet, basename="products")
router.register(r"purchases", PurchaseViewSet, basename="purchases")
router.register(r"user", UserViewSet, basename="user")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("user/login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
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
