from django.shortcuts import render
from django.utils import timezone

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.viewsets import ModelViewSet

from apps.users.models import (
    DriverProfile,
    DeliveryVehicle,
    CustomerProfile
)


from .serializers import (
    AuthTokenCustomSerializer, 
    RegisterSerializer,
    DeliveryVehicleSerializer,
    DriverProfileSerializer,
    CustomerProfileSerializer
)


# Create your views here.

class DriverProfileViewSet(ModelViewSet):
    queryset = DriverProfile.objects.all()
    serializer_class = DriverProfileSerializer


class DeliveryVehicleViewSet(ModelViewSet):
    queryset = DeliveryVehicle.objects.all()
    serializer_class = DeliveryVehicleSerializer


class CustomerProfileViewSet(ModelViewSet):
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerProfileSerializer


class GetAuthToken(ObtainAuthToken):
    """
    ---
    POST:
        serializer: AuthTokenSerializer
    """
    serializer_class = AuthTokenCustomSerializer
    permission_classes = [AllowAny]

    def get_serializer(self):
        return self.serializer_class()

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get(user=user).key

        # Update last_login of the current user
        user.last_login = timezone.now()
        user.save()

        response = {
            'token': token,
            'pk': user.pk,
            'role': user.role,
            "username": user.username,
            "email": user.email,
            "name": f"{user.first_name} {user.last_name}"
            #'view_id': user.get_view_id,
        }

        return Response(response)


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
