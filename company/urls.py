from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views
from .views import TeamDetailView

urlpatterns = [
    path("profile", views.user_profile, name="user_profile"),
    path("create_team", views.create_team, name="create_team"),
    path("show_all_teams", views.show_all_teams, name="show_all_teams"),
    path("team_detail/<int:team_id>", login_required(TeamDetailView.as_view()), name="team_detail"),
    path("manage_team_view", views.manage_team_view, name="manage_team_view"),
    path("join_team/<int:team_id>", views.join_team, name="join_team"),
    path('team/<int:team_id>/edit/', views.edit_team, name='edit_team'),
    path('teams_you_manage', views.show_teams_you_are_admin_of, name='teams_you_manage'),
    path('view_team_as_admin/<int:team_id>', views.view_team_as_admin, name='view_team_as_admin'),
]
