from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.payments.views import OrderPaymentViewSet, MpesaViewSet, LipaNaMpesaGenericAPIView

router = DefaultRouter()
router.register("order-payments", OrderPaymentViewSet, basename="order-payments")
router.register("mpesa-payments", MpesaViewSet, basename="mpesa-payments")

urlpatterns = [
    path("", include(router.urls)),
    path("lipa-na-mpesa/", LipaNaMpesaGenericAPIView.as_view(), name="lipa-na-mpesa"),
]