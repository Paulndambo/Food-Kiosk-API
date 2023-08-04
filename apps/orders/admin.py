from django.contrib import admin
from apps.orders.models import Order, OrderItem, Delivery

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["customer", "total_cost", "order_status", "payment_status"]


@admin.register(OrderItem)
class OrderItem(admin.ModelAdmin):
    list_display = ["order", "item", "quantity", "unit_price"]


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ["driver", "order", "delivered_at"]