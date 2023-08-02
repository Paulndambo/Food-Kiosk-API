from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.users.views import (
    GetAuthToken, RegisterAPI, CustomerProfileViewSet, DriverProfileViewSet, DeliveryVehicleViewSet
)

router = DefaultRouter()
router.register("drivers", DriverProfileViewSet, basename="drivers")
router.register("customers", CustomerProfileViewSet, basename="customers")
router.register("deliver-vehicles", DeliveryVehicleViewSet, basename="delivery-vehicles")


urlpatterns = [
    path("login/", GetAuthToken.as_view(), name="login"),
    path("register/", RegisterAPI.as_view(), name="register"),
    path("", include(router.urls)),
]