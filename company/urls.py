from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views
from .views import TeamDetailView

urlpatterns = [
    path("", views.index, name="index"),
    path("profile", views.user_profile, name="user_profile"),
    path("create_team", views.create_team, name="create_team"),
    path("show_all_teams", views.show_all_teams, name="show_all_teams"),
    path("team_detail/<int:team_id>", login_required(TeamDetailView.as_view()), name="team_detail"),
]
