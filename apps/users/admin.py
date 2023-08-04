from django.contrib import admin
from apps.users.models import User, CustomerProfile, DriverProfile, DeliveryVehicle
# Register your models here.
admin.site.register(User)


@admin.register(CustomerProfile)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["user", "phone_number", "gender", "town"]


@admin.register(DriverProfile)
class DriverAdmin(admin.ModelAdmin):
    list_display = ["user", "phone_number", "gender", "vehicle_type", "town"]


@admin.register(DeliveryVehicle)
class DeliveryVehicleAdmin(admin.ModelAdmin):
    list_display = ["driver", "vehicle_type", "registration_number"]