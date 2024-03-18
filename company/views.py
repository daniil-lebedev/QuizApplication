from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterTeamForm, RegisterTeamAdminForm, RegisterMemberForm
from user.forms import RegisterAbstractUserForm, LoginForm

# Create your views here.

from django.http import HttpResponse


def index(request) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the polls index.")


@login_required
def user_profile(request) -> HttpResponse:
    """
    Allows a user to view their profile.
    :param request: request for the page
    :return: response for the page
    """
    return render(request, "company/profile_page.html")
