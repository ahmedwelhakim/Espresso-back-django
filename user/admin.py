from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from user.models import User, UserAddress


class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ["email", "full_name"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal Info"),
            {
                "fields": (
                    "full_name",
                    "phone",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    readonly_fields = ["last_login"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "full_name",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


# Register your models here.


admin.site.register(User, UserAdmin)

admin.site.register(UserAddress)