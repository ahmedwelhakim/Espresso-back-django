# Create your views here.

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from user.models import UserAddress
from user.pagination import UserAddressPagination
from user.serializers import UserSerializer, UserAddressSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserAddressView(generics.CreateAPIView, generics.ListAPIView):
    serializer_class = UserAddressSerializer
    pagination_class = UserAddressPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)
