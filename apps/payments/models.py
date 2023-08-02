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
    amount_payment = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=255, choices=PAYMENT_METHOD_CHOICES)
    mpesa_data = models.JSONField(default=dict)

    def __str__(self):
        return self.payment_method