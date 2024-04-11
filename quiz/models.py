from datetime import timezone, datetime

from django.db import models
from django.urls import reverse

from company.models import Team, TeamAdmin, Member


class Quiz(models.Model):
    """
    This class represents a quiz.
    Attributes:
    title (str): The title of the quiz.
    description (str): The description of the quiz.
    created_at (datetime): The date and time the quiz was created.
    belongs_to (Company): The company the quiz belongs to.
    author (CompanyAdmin): The author of the quiz.
    due_date (datetime): The date and time the quiz is due.
    date_created (datetime): The date and time the quiz was created.
    points (int): The points of the quiz.
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    belongs_to = models.ForeignKey(Team, on_delete=models.CASCADE)
    author = models.ForeignKey(TeamAdmin, on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    @property
    def is_due(self):
        return self.due_date < datetime.now(timezone.utc)

    def get_absolute_url(self):
        return reverse("quiz_detail", kwargs={"pk": self.pk})

    def update_points(self):
        self.points = sum([question.point for question in self.question_set.all()])
        self.save()

    class Meta:
        verbose_name_plural = "quizzes"
        ordering = ["-created_at"]


class Question(models.Model):
    """
    This class represents a question.
    Attributes:
    question (str): The question.
    quiz (Quiz): The quiz the question belongs to.
    point (int): The point of the question.
    """
    question = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    point = models.IntegerField(default=0)

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse("question_detail", kwargs={"pk": self.pk})

    def update_point(self):
        self.point = sum([option.point for option in self.option_set.all()])
        self.save()

    def get_options(self):
        return self.option_set.all()

    class Meta:
        verbose_name_plural = "questions"
        ordering = ["-id"]


class Option(models.Model):
    """
    This class represents an option.
    Attributes:
    option (str): The option.
    question (Question): The question the option belongs to.
    is_correct (bool): Whether the option is correct.
    """
    option = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    point = models.IntegerField(default=0)

    def __str__(self):
        return self.option

    def get_absolute_url(self):
        return reverse("option_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name_plural = "options"
        ordering = ["-id"]


class Result(models.Model):
    """
    This class represents a result.
    Attributes:
    quiz (Quiz): The quiz the result belongs to.
    user (AbstractUser): The user who took the quiz.
    score (int): The score of the user.
    date_taken (datetime): The date and time the user took the quiz.
    """
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="results")
    score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.quiz}"

    class Meta:
        verbose_name_plural = "results"
        ordering = ["-date_taken"]
