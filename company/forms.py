from django import forms
from .models import Team, TeamAdmin, Member
from sensitivity_check.check_sensitivity import is_offensive


class RegisterTeamForm(forms.ModelForm):
    """
    This class represents the form for registering a Team.
    """

    class Meta:
        model = Team
        fields = ['name', 'description', 'email']

    def clean_name(self) -> str or None:
        """
        Check if the team name is offensive.
        :return: the team name or None if the team name is offensive
        """
        name = self.cleaned_data.get('name')
        if is_offensive(name):
            raise forms.ValidationError("The team name is offensive.")
        return name

    def clean_description(self) -> str or None:
        """
        Check if the team description is offensive.
        :return: the team description or None if the team description is offensive
        """
        description = self.cleaned_data.get('description')
        if is_offensive(description):
            raise forms.ValidationError("The team description is offensive.")
        return description

    def clean_email(self) -> str or None:
        """
        Check if the team email is offensive.
        :return: the team email or None if the team email is offensive
        """
        email = self.cleaned_data.get('email')
        if is_offensive(email):
            raise forms.ValidationError("The team email is offensive.")
        return email

    def __init__(self, *args, **kwargs):
        """
        Add warning message to the form.
        :param args:
        :param kwargs:
        """
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
