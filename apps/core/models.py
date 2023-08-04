from django.db import models

# Create your models here.
class AbstractBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Restaurant(AbstractBaseModel):
    name = models.CharField(max_length=255)
    location_description = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=255)


    def __str__(self):
        return self.name


class Menu(AbstractBaseModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title        