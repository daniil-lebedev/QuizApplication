from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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


class LoginForm(forms.Form):
    """
    This class represents the form for logging in a user.

    Attributes:
    username (CharField): The username of the user.
    password (CharField): The password of the user.
    """
    email = forms.CharField(label="Email", max_length=30, help_text="Required.", required=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput, help_text="Required.", required=True)
