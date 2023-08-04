from rest_framework import serializers
from apps.payments.models import (
    OrderPayment, 
    MpesaTransaction,
    MpesaResponseBody
)

class OrderPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPayment
        fields = "__all__"


class LipaNaMpesaSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=255)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)


class MpesaResponseBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = MpesaResponseBody
        fields = "__all__"


class MpesaTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MpesaTransaction
        fields = "__all__"
