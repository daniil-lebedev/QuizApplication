from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterTeamForm
from .models import TeamAdmin, Team
from django.views.generic import DetailView

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


@login_required
def create_team(request) -> HttpResponse or redirect:
    """
    Allows a user to create a team.
    :param request: request for the page
    :return: response for the page
    """
    team_form = RegisterTeamForm()
    if request.method == "POST":
        team_form = RegisterTeamForm(request.POST)
        if team_form.is_valid():
            # set the user as the team admin
            team = team_form.save()
            messages.success(request, "Team created successfully.")
            # create team admin without admin form
            team_admin = TeamAdmin(team=team, user=request.user)
            team_admin.save()
            messages.success(request, "Team admin created successfully.")
            return redirect("user_profile")
    context = {
        "team_form": team_form,
    }

    return render(request, "company/register_team.html", context)


@login_required
def show_all_teams(request) -> HttpResponse:
    """
    Shows all teams.
    :param request: request for the page
    :return: response for the page
    """
    teams = Team.objects.all()
    context = {
        "teams": teams,
    }
    return render(request, "company/show_all_teams.html", context)


class TeamDetailView(DetailView):
    """
    This class represents a team detail view.
    """
    model = Team
    template_name = "company/team_detail.html"
    context_object_name = "team"
    pk_url_kwarg = "team_id"

    def get_context_data(self, **kwargs) -> dict:
        """
        Get the context for the team detail view.
        :param kwargs: keyword arguments
        :return: context for the team detail view
        """
        context = super().get_context_data(**kwargs)
        team = self.get_object()
        team_admins = TeamAdmin.objects.filter(team=team)
        context["team_admins"] = team_admins
        return context
