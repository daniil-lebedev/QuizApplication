from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from user.forms import RegisterAbstractUserForm, LoginForm


# Create your views here.

def register_user(request) -> HttpResponse or redirect:
    """
    Allows a user to be created.
    :param request: request for the page
    :return: response for the page
    """
    form = RegisterAbstractUserForm()
    if request.method == "POST":
        form = RegisterAbstractUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_user")
    context = {
        "form": form,
    }

    return render(request, "security/register_as_user.html", context)


def login_user(request) -> HttpResponse or redirect:
    form = LoginForm()
    # user login logic
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            authenticated_user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if authenticated_user is not None:
                login(request, authenticated_user)
                messages.success(request, "You are now logged in.")
                return redirect("user_profile")
            else:
                messages.error(request, 'Invalid credentials')

    return render(request, 'security/login.html', {'form': form})


@login_required
def user_logout(request) -> HttpResponse or redirect:
    """
    Logs the user out.
    :param request:
    :return:
    """
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('login_user')
