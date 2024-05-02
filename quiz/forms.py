from company.models import Team
from education_board.models import Board
from .models import Quiz, Question, Option
from django import forms
from sensitivity_check.check_sensitivity import is_offensive


class CreateQuizForm(forms.ModelForm):
    """
    This class represents the form for creating a Quiz.
    """

    class Meta:
        model = Quiz
        fields = ['title', 'description', 'due_date', 'belongs_to', 'educational_board']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'belongs_to': forms.Select(attrs={'class': 'form-control'}),
            'educational_board': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_title(self) -> str:
        """
        This function checks if the title contains any offensive words.
        :return: title of the quiz
        """
        title = self.cleaned_data.get('title')
        if is_offensive(title):
            raise forms.ValidationError("Title contains offensive words")
        return title

    def clean_description(self) -> str:
        """
        This function checks if the description contains any offensive words.
        :return: description of the quiz
        """
        description = self.cleaned_data.get('description')
        if is_offensive(description):
            raise forms.ValidationError("Description contains offensive words")
        return description

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Extract user from kwargs to avoid passing it to the superclass
        super(CreateQuizForm, self).__init__(*args, **kwargs)
        if user:
            # Set the queryset for 'belongs_to' to only include teams where the user is an admin
            self.fields['belongs_to'].queryset = Team.objects.filter(team_of_admin__user=user)
            # Set the queryset for 'educational_board' to include boards related to teams where the user is an admin
            self.fields['educational_board'].queryset = Board.objects.filter(team__team_of_admin__user=user)


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
