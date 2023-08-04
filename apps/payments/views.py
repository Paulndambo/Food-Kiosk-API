from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status, generics


from apps.payments.serializers import (
    OrderPaymentSerializer, 
    LipaNaMpesaSerializer,
    MpesaResponseBodySerializer,
    MpesaTransactionSerializer
)
from apps.payments.models import OrderPayment, MpesaTransaction, MpesaResponseBody

from apps.payments.utils import MpesaGateWay
from apps.payments.mpesa_metadata_transformer import mpesa_metadata_transformative_function
# Create your views here.
class OrderPaymentViewSet(ModelViewSet):
    queryset = OrderPayment.objects.all()
    serializer_class = OrderPaymentSerializer


class LipaNaMpesaGenericAPIView(generics.CreateAPIView):
    serializer_class = LipaNaMpesaSerializer

    def post(self, request, *args, **kwargs):
        data = request.data 
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            cl = MpesaGateWay()
            cl.stk_push(
                phone_number=data.get('phone_number'),
                amount=int(data.get('amount')),
                callback_url="https://f2dc-105-160-76-83.ngrok-free.app/payments/mpesa-payments/",
                account_reference="Perfin Mpesa",
                transaction_desc="This is perfin mpesa transaction"
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"failed": "Payment Request Failed!!"}, status=status.HTTP_400_BAD_REQUEST)


class MpesaViewSet(ModelViewSet):
    queryset = MpesaResponseBody.objects.all()
    serializer_class = MpesaResponseBodySerializer

    def create(self, request, *args, **kwargs):
        body = request.data["Body"]
        
        if body:
            mpesa = MpesaResponseBody.objects.create(body=body)
            transformed_mpesa_response = mpesa_metadata_transformative_function(body['stkCallback'])
            serializer = MpesaTransactionSerializer(data=transformed_mpesa_response)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({"failed": "Transaction Failed"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"failed": "The Transaction has not send callback data"}, status=status.HTTP_400_BAD_REQUEST)
