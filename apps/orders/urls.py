from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.orders.views import OrderItemViewSet, OrderViewSet, DeliveryViewSet

router = DefaultRouter()
router.register("orders", OrderViewSet, basename="orders")
router.register("order-items", OrderItemViewSet, basename="order-items")
router.register("deliveries", DeliveryViewSet, basename="deliveries")

urlpatterns = [
    path("", include(router.urls)),
]