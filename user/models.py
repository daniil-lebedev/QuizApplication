# accounts/models.py
from .manager import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class AbstractUser(AbstractBaseUser, PermissionsMixin):
    """
    This class represents the custom user model.

    Attributes:
    email (str): The email of the user.
    first_name (str): The first name of the user.
    last_name (str): The last name of the user.
    is_active (bool): Whether the user is active.
    is_staff (bool): Whether the user is staff.
    created_at (datetime): The date and time the user was created.
    """
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    groups = None
    user_permissions = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
