from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from quiz.models import Quiz
from .forms import RegisterTeamForm
from .models import TeamAdmin, Team, Member
from django.views.generic import DetailView

from django.http import HttpResponse


def index(request) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the polls index.")


@login_required
def user_profile(request) -> HttpResponse:
    """
    Allows a user to view their profile, including quizzes for their administered teams.
    :param request: request for the page
    :return: response for the page
    """
    # Get the teams where the user is an admin
    user_teams = Team.objects.filter(team_of_admin__user=request.user).distinct()

    # get teams where the user is a member
    user_teams_member_of = user_teams.union(Team.objects.filter(team_of_member__user=request.user).distinct())

    # Filter quizzes that belong to any of the teams the user administers
    quizzes = Quiz.objects.filter(belongs_to__in=user_teams).distinct()

    context = {
        "quizzes": quizzes,
        "user_teams_member_of": user_teams_member_of,
    }

    return render(request, "company/profile_page.html", context)


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


def show_all_teams(request):
    teams = Team.objects.all()

    for team in teams:
        team.can_join = not (team.team_of_admin.filter(user=request.user).exists() or
                             team.team_of_member.filter(user=request.user).exists())

    return render(request, 'company/show_all_teams.html', {'teams': teams})


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


@login_required
def manage_team_view(request) -> render:
    """
    Allows a user to manage a company.
    :param request: request for the page
    :return: response for the page
    """
    # get all the teams for the specific user
    teams = request.user.team_admins.all()
    context = {
        "teams": teams,
    }
    return render(request, "company/manage_team.html", context)


@login_required
def edit_team(request, team_id):
    """
    View function to edit an existing Team.
    :param request: HttpRequest object
    :param team_id: ID of the Team to edit
    :return: HttpResponse object with the team edit form
    """
    team = get_object_or_404(Team, id=team_id)

    # Check if the current user is allowed to edit the team
    # This check assumes you have a way to determine if the user is an admin of the team
    if not team.team_of_admin.filter(user=request.user).exists():
        # Handle unauthorized access, e.g., by showing an error message or redirecting
        return redirect('unauthorized_access_url')  # Replace with an appropriate response

    if request.method == 'POST':
        form = RegisterTeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            # Redirect to a success page, such as the team detail view
            return redirect('team_detail', team_id=team.id)
    else:
        form = RegisterTeamForm(instance=team)

    context = {
        'form': form,
        'team': team
    }
    return render(request, 'company/edit_team.html', context)


@login_required
def join_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    # Attempt to get the first admin for the team
    admin_relation = TeamAdmin.objects.filter(team=team).first()
    print(admin_relation)

    if not Member.objects.filter(team=team, user=request.user).exists():
        if admin_relation:
            # Create a new member with the first admin found as the manager
            Member.objects.create(team=team, user=request.user, managed_by=admin_relation)
            messages.success(request, "You have successfully joined the team.")
        else:
            # If no admin is found, an error message is displayed
            messages.error(request, "The team does not have an admin.")
    else:
        messages.error(request, "You are already a member of this team.")

    return redirect('team_detail', team_id=team_id)
