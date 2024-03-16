from django.db import models
from django.urls import reverse

from user.models import AbstractUser


class Team(models.Model):
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
        return reverse("team_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name_plural = "teams"
        ordering = ["-created_at"]


class TeamAdmin(models.Model):
    """
    This class represents a company admin.

    Attributes:
    company (Company): The company the admin belongs to.
    user (User): The user who is the admin of the company.
    created_at (datetime): The date and time the company admin was created.
    updated_at (datetime): The date and time the company admin was last updated.
    """
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(AbstractUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user} - {self.team}"

    class Meta:
        verbose_name_plural = "team admins"
        ordering = ["-created_at"]


class Member(models.Model):
    """
    This class represents a worker.

    Attributes:
    company (Company): The company the worker belongs to.
    managed_by (CompanyAdmin): The company admin who manages the worker.
    user (User): The user who is the worker of the company.
    created_at (datetime): The date and time the worker was created.
    updated_at (datetime): The date and time the worker was last updated.
    """
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    managed_by = models.ForeignKey(TeamAdmin, on_delete=models.CASCADE)
    user = models.ForeignKey(AbstractUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user} - {self.team}"

    class Meta:
        verbose_name_plural = "Members"
        ordering = ["-created_at"]
