from django.db import models
from apps.core.models import AbstractBaseModel
# Create your models here.
PAYMENT_METHOD_CHOICES = (
    ("mpesa", "Mpesa"),
    ("cash", "Cash"),
    ("credit", "Credit"),
)

class OrderPayment(AbstractBaseModel):
    order = models.ForeignKey("orders.Order", on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=255, choices=PAYMENT_METHOD_CHOICES)
    mpesa_data = models.JSONField(default=dict)

    def __str__(self):
        return self.payment_method


class MpesaResponseBody(AbstractBaseModel):
    body = models.JSONField()


class MpesaTransaction(AbstractBaseModel):
    receipt_number = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    merchant_request_id = models.CharField(max_length=255)
    checkout_request_id = models.CharField(max_length=255)
    transaction_result_code = models.CharField(max_length=255)
    transaction_timestamp = models.FloatField()

    def __str__(self):
        return self.phone_number + " has paid " + str(self.amount)
