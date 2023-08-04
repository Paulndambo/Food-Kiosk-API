from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from apps.core.models import Restaurant, Menu
from apps.core.serializers import MenuSerializer, RestaurantSerializer

# Create your views here.
class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer