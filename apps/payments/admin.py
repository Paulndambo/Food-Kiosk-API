from django.contrib import admin
from apps.payments.models import OrderPayment
# Register your models here.
@admin.register(OrderPayment)
class OrderPaymentAdmin(admin.ModelAdmin):
    list_display = ["order", "phone_number", "amount_paid", "payment_method", "mpesa_data"]