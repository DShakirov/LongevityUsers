import random
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from django.conf import settings
from .managers import EmailPhoneUserManager


class Device(models.Model):
    """
    Device model used for permanent token authentication
    """

    permanent_token = models.CharField(max_length=255, unique=True)
    jwt_secret = models.UUIDField(default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="devices"
    )
    name = models.CharField(_("Device name"), max_length=255)
    details = models.CharField(_("Device details"), max_length=255, blank=True)
    last_request_datetime = models.DateTimeField(auto_now=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Device")
        verbose_name_plural = _("Devices")
        ordering = ["-ip_address"]


class AbstractEmailPhoneUser(AbstractBaseUser, PermissionsMixin):

    cognito_username = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    username = models.CharField(
        _("email or phone"),
        max_length=255,
        unique=True,
        blank=True,
        db_index=True,
        help_text=_(
            "Required. 255 characters or fewer. Letters, digits and " "@/./+/-/_ only."
        ),
        validators=[
            validators.RegexValidator(
                r"^[\w.@+-]+$",
                _(
                    "Enter a valid username. "
                    "This value may contain only letters, numbers "
                    "and @/./+/-/_ characters."
                ),
                "invalid",
            ),
        ],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    image = models.ImageField(_("image"), blank=True, null=True,  upload_to="images/")
    first_name = models.CharField(_("first name"), max_length=30, blank=True, null=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True, null=True)
    email = models.EmailField(_("email"), max_length=254, blank=True)
    is_doctor = models.BooleanField(default=False)
    is_used = models.BooleanField(default=False)
    phone_number = models.CharField(_("phone"), max_length=255, blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    user_device = models.ForeignKey(
        Device, on_delete=models.CASCADE, related_name="user_device", null=True
    )
    date_locked = models.DateTimeField(null=True, blank=True)

    objects = EmailPhoneUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email or ""


class CustomUser(AbstractEmailPhoneUser):

    """Concrete class of AbstractEmailPhoneUser.
    Use this if you don't need to extend CustomUser.
    """

    class Meta(AbstractEmailPhoneUser.Meta):
        swappable = "AUTH_USER_MODEL"

