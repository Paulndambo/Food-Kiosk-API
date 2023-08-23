from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from apps.core.models import AbstractBaseModel

from rest_framework.authtoken.models import Token
# Create your models here.
ROLE_CHOICES = (
    ("admin", "Admin"),
    ("driver", "Driver"),
    ("cashier", "Cashier"),
    ("customer", "Customer"),
)


GENDER_CHOICES = (
    ("male", "Male"),
    ("female", "Female"),
)


VEHICLE_TYPE_CHOICES = (
    ("car", "Car"),
    ("bike", "Bike"),
)


class User(AbstractUser, AbstractBaseModel): 
    role = models.CharField(choices=ROLE_CHOICES, max_length=32)
    
    def __str__(self):
        return self.username


class CustomerProfile(AbstractBaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    location_description = models.CharField(max_length=500)
    town = models.CharField(max_length=255)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True)

    def __str__(self):
        return self.user.username


class DriverProfile(AbstractBaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    vehicle_type = models.CharField(max_length=255, choices=VEHICLE_TYPE_CHOICES)
    location_description = models.CharField(max_length=500)
    driving_licence = models.FileField(upload_to="driving_licences/", null=True)
    town = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


class DeliveryVehicle(AbstractBaseModel):
    driver = models.OneToOneField(DriverProfile, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=255, choices=VEHICLE_TYPE_CHOICES)
    registration_number = models.CharField(max_length=255)
    vehicle_image = models.ImageField(upload_to="vehicle_images/", null=True)

    def __str__(self):
        return self.registration_number
    

@receiver(post_save, sender=User)
def create_user_token(sender, instance, created, **kwargs):
    if created:
        token = Token.objects.create(user=instance)