from django.contrib.auth.forms import UserCreationForm
from sensitivity_check.check_sensitivity import is_offensive
from .models import AbstractUser
from django import forms


class RegisterAbstractUserForm(UserCreationForm):
    """
    This class represents the form for registering an abstract user.

    Attributes:
    first_name (CharField): The first name of the user.
    last_name (CharField): The last name of the user.
    email (EmailField): The email of the user.
    password1 (CharField): The first password field.
    password2 (CharField): The second password field.
    """
    first_name = forms.CharField(max_length=30, required=False, help_text="Optional.")
    last_name = forms.CharField(max_length=30, required=False, help_text="Optional.")
    email = forms.EmailField(max_length=254, help_text="Required. Inform a valid email address.")

    class Meta:
        model = AbstractUser
        fields = ["email", "first_name", "last_name", "email", "password1", "password2"]

    def clean_first_name(self) -> str or None:
        """
        Check if the first name is offensive.
        :return: the first name or None if the first name is offensive
        """
        first_name = self.cleaned_data.get('first_name')
        analyzed_text = is_offensive(first_name)
        if analyzed_text['is_offensive']:
            raise forms.ValidationError("Content contains offensive content. Reason: " + analyzed_text['reason'])
        return first_name

    def clean_last_name(self) -> str or None:
        """
        Check if the last name is offensive.
        :return: the last name or None if the last name is offensive
        """
        last_name = self.cleaned_data.get('last_name')
        analyzed_text = is_offensive(last_name)
        if analyzed_text['is_offensive']:
            raise forms.ValidationError("Content contains offensive content. Reason: " + analyzed_text['reason'])
        return last_name

    def clean_email(self) -> str or None:
        """
        Check if the email is offensive.
        :return: the email or None if the email is offensive
        """
        email = self.cleaned_data.get('email')
        analyzed_text = is_offensive(email)
        if analyzed_text['is_offensive']:
            raise forms.ValidationError("Content contains offensive content. Reason: " + analyzed_text['reason'])
        return email

    def __init__(self, *args, **kwargs):
        """
        Add warning message to the form.
        :param args:
        :param kwargs:
        """
        super(RegisterAbstractUserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})


class LoginForm(forms.Form):
    """
    This class represents the form for logging in a user.

    Attributes:
    username (CharField): The username of the user.
    password (CharField): The password of the user.
    """
    email = forms.CharField(label="Email", max_length=40, help_text="Required.", required=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput, help_text="Required.", required=True)
