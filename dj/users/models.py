from django.db import models
from django.core.validators import RegexValidator
from django.contrib.postgres import fields as pg_fields
from django.utils.translation import ugettext as _
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)

# Create your models here.

validate_mobile = RegexValidator(
    regex=r"\d{10}", message=_("Enter a valid indian mobile number.")
)


class UserManager(BaseUserManager):
    def create_user(self, phone, password: None):
        if not phone:
            raise ValueError("User must have a phone")
        user = self.model(phone=phone)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password=None):
        user = self.create_user(phone, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(
        max_length=20, validators=[validate_mobile], null=True, unique=True
    )
    email = pg_fields.CIEmailField(blank=True, null=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("People who are the part of organisation."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_("Designates whether this user should be treated as active."),
    )
    is_admin = models.BooleanField(
        _("admin"),
        default=False,
        help_text=_("Whether the user is admin of site or not."),
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = "phone"

    objects = UserManager()

    @property
    def full_name(self):
        return self.get_full_name()

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip() or self.phone

    def __str__(self):
        return self.get_full_name()
