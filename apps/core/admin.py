from django.contrib import admin
from apps.core.models import Restaurant, Menu
# Register your models here.
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ["name", "location_description", "phone_number"]


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ["restaurant", "name", "price", "available"]