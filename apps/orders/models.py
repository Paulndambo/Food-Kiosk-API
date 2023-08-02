from django.db import models
from apps.core.models import AbstractBaseModel
# Create your models here.
ORDER_STATUS_CHOICES = (
    ("processing", "Processing"),
    ("cancelled", "Cancelled"),
    ("delivered", "Delivered"),
    ("disputed", "Disputed"),
)

PAYMENT_STATUS_CHOICES = (
    ("pending", "Pending"),
    ("paid", "Paid"),
)

class Order(AbstractBaseModel):
    customer = models.ForeignKey("users.CustomerProfile", on_delete=models.SET_NULL, null=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=255, choices=ORDER_STATUS_CHOICES, default="processing")
    payment_status = models.CharField(max_length=255, choices=PAYMENT_STATUS_CHOICES, default="pending")

    def __str__(self):
        return self.customer.user.username


class OrderItem(AbstractBaseModel):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name="orderitems")
    item = models.ForeignKey("core.Menu", on_delete=models.PROTECT, related_name="menuitems")
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item.title


class Delivery(AbstractBaseModel):
    driver = models.ForeignKey("users.DriverProfile", on_delete=models.PROTECT, related_name="deliveries")
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    delivered_at = models.DateTimeField()

    def __str__(self):
        return str(self.id)