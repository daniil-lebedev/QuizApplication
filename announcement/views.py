from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView

from company.models import Team, TeamAdmin
from .forms import CreateAnnouncementForm, CreateComment, CreateAdminCommentForm
from .models import Announcement


# Create your views here.
class AnnouncementDetailView(DetailView):
    """
    View for an announcement detail.

    """
    model = Announcement
    template_name = "announcement/view_announcement.html"
    context_object_name = "announcement"

    def get_context_data(self, **kwargs) -> dict:
        """
        Gets the context for the announcement detail.
        :param kwargs:
        :return:
        """
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comment_set.all()
        return context


@login_required
def create_announcement(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    user = request.user

    # Ensure the user is a TeamAdmin for the specified team
    team_admin = TeamAdmin.objects.filter(user=user, team=team).first()
    if not team_admin:
        messages.error(request, "You are not authorized to create announcements for this team.")
        return redirect('team_list')  # Redirect to a list of teams or an appropriate error page

    if request.method == "POST":
        form = CreateAnnouncementForm(request.POST, team=team)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.team = team
            announcement.created_by = team_admin
            announcement.save()
            messages.success(request, "Announcement created successfully.")
            return redirect(announcement.get_absolute_url())
    else:
        form = CreateAnnouncementForm(team=team)

    return render(request, "announcement/create_announcement.html", {"form": form})


@login_required
def view_all_announcements(request) -> render:
    """
    Allows a user to view all announcements.
    :param request:
    :return:
    """
    announcements = Announcement.objects.all()
    return render(request, "announcement/view_all_announcements.html", {"announcements": announcements})


@login_required
def create_comment(request, pk) -> render:
    """
    Allows a user to create a comment.
    :param request:
    :param pk:
    :return:
    """
    form = CreateComment()
    announcement = Announcement.objects.get(pk=pk)
    if request.method == "POST":
        form = CreateComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.announcement = announcement
            comment.created_by = request.user.team_member.first()
            form.save()
            return redirect("announcement_detail", pk=pk)
    return render(request, "announcement/create_comment.html", {"form": form})


@login_required
def create_admin_comment(request, pk) -> render:
    """
    Allows a user to create a comment.
    :param request:
    :param pk:
    :return:
    """
    form = CreateAdminCommentForm()
    announcement = Announcement.objects.get(pk=pk)
    if request.method == "POST":
        form = CreateAdminCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.announcement = announcement
            comment.created_by = request.user.team_admins.first()
            form.save()
            messages.success(request, "Comment created successfully")
            return redirect("announcement_detail", pk=pk)
    return render(request, "announcement/create_comment.html", {"form": form})
