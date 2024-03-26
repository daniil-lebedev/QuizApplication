from .models import Quiz, Question, Option
from django import forms


class CreateQuizForm(forms.ModelForm):
    """
    This class represents the form for creating a Quiz.
    """

    class Meta:
        model = Quiz
        fields = ['title', 'description', 'due_date', 'belongs_to']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'belongs_to': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(CreateQuizForm, self).__init__(*args, **kwargs)


class CreateQuestionForm(forms.ModelForm):
    """
    This class represents the form for creating a Question.
    """

    class Meta:
        model = Question
        fields = ['question', 'quiz']
        widgets = {
            'question': forms.Textarea(attrs={'class': 'form-control'}),
            'quiz': forms.Select(attrs={'class': 'form-control'}),
        }

    # add warning message to the form
    def __init__(self, *args, **kwargs):
        super(CreateQuestionForm, self).__init__(*args, **kwargs)
        self.fields['question'].widget.attrs.update({'class': 'form-control'})
        self.fields['quiz'].widget.attrs.update({'class': 'form-control'})


class CreateOptionForm(forms.ModelForm):
    """
    This class represents the form for creating an Option.
    """

    class Meta:
        model = Option
        fields = ['option', 'question', 'is_correct', 'point']

    # add warning message to the form
    def __init__(self, *args, **kwargs):
        super(CreateOptionForm, self).__init__(*args, **kwargs)
        self.fields['option'].widget.attrs.update({'class': 'form-control'})
        self.fields['question'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_correct'].widget.attrs.update({'class': 'form-control'})
        self.fields['point'].widget.attrs.update({'class': 'form-control'})
