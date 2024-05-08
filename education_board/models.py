from django.db import models

from company.models import Team


# Create your models here.
class Board(models.Model):
    """
    Education Board model for providing information about the education board.

    Attributes:
    title: A CharField representing the title of the education board.
    description: A TextField representing the description of the education board.
    date_created: A DateTimeField representing the date the education board was created.
    date_updated: A DateTimeField representing the date the education board was last updated.
    """
    title = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='boards_of_team')
    created_by = models.ForeignKey('company.TeamAdmin', on_delete=models.CASCADE, related_name='created_by_boards')
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Slide(models.Model):
    """
    Slide model for providing information about the slide.

    Attributes:
    title: A CharField representing the title of the slide.
    description: A TextField representing the description of the slide.
    date_created: A DateTimeField representing the date the slide was created.
    date_updated: A DateTimeField representing the date the slide was last updated.
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='slides')
    # future update
    #image = models.ImageField(upload_to='slides/')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
