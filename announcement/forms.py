from company.models import TeamAdmin
from quiz.models import Quiz
from .models import Announcement, AdminComment, Comment
from sensitivity_check.check_sensitivity import is_offensive
from django import forms


class CreateAnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'description', 'quiz']

    def clean_title(self) -> str:
        """
        Check if the title contains offensive content.
        :return: title of the announcement
        """
        title = self.cleaned_data['title']
        analyzed_text = is_offensive(title)
        if analyzed_text['is_offensive']:
            raise forms.ValidationError("Content contains offensive content. Reason: " + analyzed_text['reason'])
        return title

    def clean_description(self) -> str:
        """
        Check if the description contains offensive content.
        :return: description of the announcement
        """
        description = self.cleaned_data['description']
        analyzed_text = is_offensive(description)
        if analyzed_text['is_offensive']:
            raise forms.ValidationError("Content contains offensive content. Reason: " + analyzed_text['reason'])
        return description

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

    def clean_content(self):
        """
        Check if the content contains offensive content.
        :return: content of the admin comment
        """
        content = self.cleaned_data['content']
        analyzed_text = is_offensive(content)
        if analyzed_text['is_offensive']:
            raise forms.ValidationError("Content contains offensive content. Reason: " + analyzed_text['reason'])
        return content

    def __init__(self, *args, **kwargs):
        super(CreateAdminCommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = "Comment"


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

    def clean_content(self):
        """
        Check if the content contains offensive content.
        :return: content of the comment
        """
        content = self.cleaned_data['content']
        analyzed_text = is_offensive(content)
        if analyzed_text['is_offensive']:
            raise forms.ValidationError("Content contains offensive content. Reason: " + analyzed_text['reason'])
        return content

    def __init__(self, *args, **kwargs):
        super(CreateComment, self).__init__(*args, **kwargs)
        self.fields['content'].label = "Comment"
        self.fields['content'].widget.attrs['placeholder'] = "Write a comment..."
