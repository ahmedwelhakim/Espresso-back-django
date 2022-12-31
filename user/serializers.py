from django.contrib.auth import get_user_model
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from user.models import UserAddress


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["email", "password", "full_name", "phone"]
        extra_kwargs = {
            "password": {
                "write_only": True,
                "min_length": 6,
            }
        }

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    phone = PhoneNumberField(region="EG")


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        # fields = '__all__'
        exclude = ["user"]

    def create(self, validated_data):
        request = self.context.get("request")
        if not UserAddress.objects.filter(user=request.user).exists():
            validated_data["is_default"] = True
        else:
            validated_data["is_default"] = False
        user_address = UserAddress.objects.create(
            user_id=request.user.id, **validated_data
        )
        return user_address

    phone = PhoneNumberField(region="EG")
