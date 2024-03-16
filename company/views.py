from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegisterTeamForm, RegisterTeamAdminForm, RegisterMemberForm
from user.forms import RegisterAbstractUserForm, LoginForm

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
    user_form = RegisterAbstractUserForm()
    if request.method == "POST":
        user_form = RegisterAbstractUserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect("login_user")
    context = {
        "user_form": user_form,
    }

    return render(request, "company/register_company_and_admin.html", context)


def login_user(request):
    form = LoginForm()
    # user login logic
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            authenticated_user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            print(authenticated_user is not None)
            if authenticated_user is not None:
                login(request, authenticated_user)
                messages.success(request, "You are now logged in.")
                return redirect("user_profile")
            else:
                messages.error(request, 'Invalid credentials')

    return render(request, 'company/login.html', {'form': form})


def user_profile(request) -> HttpResponse:
    """
    Allows a user to view their profile.
    :param request: request for the page
    :return: response for the page
    """
    return render(request, "company/profile_page.html")
