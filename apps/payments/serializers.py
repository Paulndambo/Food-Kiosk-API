from rest_framework import serializers
from apps.payments.models import OrderPayment

class OrderPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPayment
        fields = "__all__"