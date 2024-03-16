from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Team, TeamAdmin, Member


class RegisterTeamForm(forms.ModelForm):
    """
    This class represents the form for registering a Team.
    """
    class Meta:
        model = Team
        fields = ['name', 'description', 'email']

    # add warning message to the form
    def __init__(self, *args, **kwargs):
        super(RegisterTeamForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})


class RegisterTeamAdminForm(forms.ModelForm):
    """
    This class represents the form for registering a Team admin.
    """
    class Meta:
        model = TeamAdmin
        fields = ['team', 'user']

    # add warning message to the form
    def __init__(self, *args, **kwargs):
        super(RegisterTeamAdminForm, self).__init__(*args, **kwargs)
        self.fields['team'].widget.attrs.update({'class': 'form-control'})
        self.fields['user'].widget.attrs.update({'class': 'form-control'})


class RegisterMemberForm(forms.ModelForm):
    """
    This class represents the form for registering a Member.
    """
    class Meta:
        model = Member
        fields = ['team', 'user']

    # add warning message to the form
    def __init__(self, *args, **kwargs):
        super(RegisterMemberForm, self).__init__(*args, **kwargs)
        self.fields['team'].widget.attrs.update({'class': 'form-control'})
        self.fields['user'].widget.attrs.update({'class': 'form-control'})
