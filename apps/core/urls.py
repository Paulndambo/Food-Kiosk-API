from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.core.views import RestaurantViewSet, MenuViewSet

router = DefaultRouter()
router.register("restaurants", RestaurantViewSet, basename="restaurants")
router.register("menus", MenuViewSet, basename="menus")

urlpatterns = [
    path("", include(router.urls)),
]