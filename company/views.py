from django.shortcuts import render
from .forms import RegisterCompanyForm, RegisterCompanyAdminForm, RegisterWorkerForm
from user.forms import RegisterAbstractUserForm

# Create your views here.

from django.http import HttpResponse


def index(request) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the polls index.")


def register_user(request) -> HttpResponse:
    """
    Allows a user to be created.
    :param request: request for the page
    :return: response for the page
    """
    admin_form = RegisterAbstractUserForm()
    if request.method == "POST":
        admin_form = RegisterAbstractUserForm(request.POST)
        if admin_form.is_valid():
            admin_form.save()
    context = {
        "admin_form": admin_form,
    }

    return render(request, "company/register_company_and_admin.html", context)
