from .models import Announcement, AdminComment, Comment

from django import forms


class CreateAnnouncementForm(forms.ModelForm):
    """
    Form for creating an announcement.
    """
    class Meta:
        model = Announcement
        fields = ['title', 'description', 'quiz', 'company']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'quiz': forms.Select(attrs={'class': 'form-control'}),
            'company': forms.Select(attrs={'class': 'form-control'}),
        }


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
