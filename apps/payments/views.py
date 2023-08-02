from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from apps.payments.serializers import OrderPaymentSerializer
from apps.payments.models import OrderPayment
# Create your views here.
class OrderPaymentViewSet(ModelViewSet):
    queryset = OrderPayment.objects.all()
    serializer_class = OrderPaymentSerializer