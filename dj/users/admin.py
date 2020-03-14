from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission
import users.models as m

# Register your models here.


admin.site.register(Permission)


@admin.register(m.User)
class ShankaraUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("phone", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "email")}),
        (
            "Permissions",
            {"fields": ("is_superuser", "is_staff", "is_active", "user_permissions")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "phone",
                    "password1",
                    "password2",
                ),
            },
        ),
    )

    list_display = ("phone", "first_name", "last_name", "email", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("phone", "first_name", "last_name", "email")
    ordering = ("first_name", "last_name", "email")
