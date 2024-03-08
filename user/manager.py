from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    This class represents the custom user manager.

    Attributes:
    None

    Methods:
    create_user: Create a new user.
    create_superuser: Create a new superuser.
    """

    def create_abstract_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_abstract_user(email, password, **extra_fields)

    @property
    def company_admin_set(self):
        return self.companyadmin_set.all()

    @property
    def worker_set(self):
        return self.worker_set.all()
