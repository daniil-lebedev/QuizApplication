from company.models import TeamAdmin
from quiz.models import Quiz
from .models import Announcement, AdminComment, Comment

from django import forms


class CreateAnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'description', 'quiz']  # Exclude 'team' and 'created_by' from the form fields

    def __init__(self, *args, team=None, **kwargs):
        super(CreateAnnouncementForm, self).__init__(*args, **kwargs)
        self.team = team
        if team:
            self.fields['quiz'].queryset = Quiz.objects.filter(belongs_to=team)

    def save(self, commit=True):
        instance = super(CreateAnnouncementForm, self).save(commit=False)
        if commit:
            instance.save()  # Save the instance first to handle many-to-many relations if needed
            self.save_m2m()
        return instance


class CreateAdminCommentForm(forms.ModelForm):
    """
    Form for creating an admin comment.
    """

    class Meta:
        model = AdminComment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CreateComment(forms.ModelForm):
    """
    Form for creating a comment.
    """

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
