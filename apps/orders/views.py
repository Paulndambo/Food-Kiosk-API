from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from apps.orders.models import Order, OrderItem, Delivery
from apps.orders.serializers import DeliverySerializer, OrderItemSerializer, OrderSerializer
# Create your views here.
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class DeliveryViewSet(ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer