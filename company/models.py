from django.db import models
from django.urls import reverse


class Company(models.Model):
    """
    This class represents a company.

    Attributes:
    name (str): The name of the company.
    description (str): The description of the company.
    email (str): The email of the company.
    created_at (datetime): The date and time the company was created.
    updated_at (datetime): The date and time the company was last updated.
    """
    name = models.CharField(max_length=200)
    description = models.TextField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        # return the url for the company detail page
        return reverse("company_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name_plural = "companies"
        ordering = ["-created_at"]


class Admin(models.Model):
    """
    This class represents an admin.

    Attributes:
    first_name (str): The first name of the admin.
    last_name (str): The last name of the admin.
    email (str): The email of the admin.
    created_at (datetime): The date and time the admin was created.
    updated_at (datetime): The date and time the admin was last updated.
    """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="admins")
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name_plural = "admins"
        ordering = ["-created_at"]
