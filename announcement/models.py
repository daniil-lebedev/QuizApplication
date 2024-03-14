from django.db import models
from django.urls import reverse

from company.models import CompanyAdmin, Worker
from quiz.models import Quiz


class Announcement(models.Model):
    """
    This class represents an announcement.

    Attributes:
    title (str): The title of the announcement.
    description (str): The description of the announcement.
    created_at (datetime): The date and time the announcement was created.
    quiz (Quiz): The quiz the announcement belongs to.
    created_by (CompanyAdmin): The company admin who created the announcement.
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created_by = models.ForeignKey(CompanyAdmin, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse("announcement_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name_plural = "announcements"
        ordering = ["-created_at"]


class Comment(models.Model):
    """
    This class represents a comment.

    Attributes:
    content (str): The content of the comment.
    created_at (datetime): The date and time the comment was created.
    announcement (Announcement): The announcement the comment belongs to.
    created_by (CompanyAdmin): The company worker who created the comment.
    """
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    created_by = models.ForeignKey(Worker, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.content

    class Meta:
        verbose_name_plural = "comments"
        ordering = ["-created_at"]


class AdminComment(models.Model):
    """
    This class represents a comment.

    Attributes:
    content (str): The content of the comment.
    created_at (datetime): The date and time the comment was created.
    announcement (Announcement): The announcement the comment belongs to.
    created_by (CompanyAdmin): The company worker who created the comment.
    """
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    created_by = models.ForeignKey(CompanyAdmin, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.content

    class Meta:
        verbose_name_plural = "admin comments"
        ordering = ["-created_at"]
