from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

from django.contrib.contenttypes.models import ContentType
from django.db import models


from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_field):
        if not email:
            raise ValueError("User must have an email address. ")
        user = self.model(email=email.lower(), **extra_field)
        user.is_guest = False
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255)
    phone = PhoneNumberField(null=True, blank=True, unique=True, region="EG")

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_guest = models.BooleanField(default=True)

    objects = UserManager()
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.full_name


class UserAddress(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_address"
    )
    name = models.CharField(max_length=255)
    phone = PhoneNumberField(null=True, blank=True, region="EG")
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    building = models.CharField(max_length=255)
    floor = models.CharField(max_length=255)
    apartment = models.CharField(max_length=255)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"user: {self.user.full_name}, name: {self.name}"
