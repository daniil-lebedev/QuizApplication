from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Company, CompanyAdmin, Worker


class RegisterCompanyForm(forms.ModelForm):
    """
    This class represents the form for registering a company.
    """
    class Meta:
        model = Company
        fields = ['name', 'description', 'email']

    # add warning message to the form
    def __init__(self, *args, **kwargs):
        super(RegisterCompanyForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})


class RegisterCompanyAdminForm(forms.ModelForm):
    """
    This class represents the form for registering a company admin.
    """
    class Meta:
        model = CompanyAdmin
        fields = ['company', 'user']

    # add warning message to the form
    def __init__(self, *args, **kwargs):
        super(RegisterCompanyAdminForm, self).__init__(*args, **kwargs)
        self.fields['company'].widget.attrs.update({'class': 'form-control'})
        self.fields['user'].widget.attrs.update({'class': 'form-control'})


class RegisterWorkerForm(forms.ModelForm):
    """
    This class represents the form for registering a worker.
    """
    class Meta:
        model = Worker
        fields = ['company', 'user']

    # add warning message to the form
    def __init__(self, *args, **kwargs):
        super(RegisterWorkerForm, self).__init__(*args, **kwargs)
        self.fields['company'].widget.attrs.update({'class': 'form-control'})
        self.fields['user'].widget.attrs.update({'class': 'form-control'})
