from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "email",
        "name",
        "social_account_type",
        "is_staff",
        "is_active",
        "date_joined",
    )
    search_fields = ("email", "name")
    ordering = ("email",)
    filter_horizontal = ()
    list_filter = ("social_account_type", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("name", "social_account_type")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important Dates", {"fields": ("date_joined",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "name",
                    "social_account_type",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
