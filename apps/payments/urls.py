from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.payments.views import OrderPaymentViewSet

router = DefaultRouter()
router.register("order-payments", OrderPaymentViewSet, basename="order-payments")

urlpatterns = [
    path("", include(router.urls)),
]