from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import DetailView

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
def create_announcement(request) -> render:
    """
    Allows a user to create an announcement.
    :param request:
    :return:
    """
    form = CreateAnnouncementForm()
    if request.method == "POST":
        form = CreateAnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            # set the team admin who created the announcement
            announcement.created_by = request.user.team_admins.first()
            form.save()
            # redirect to the announcement detail page
            return redirect("announcement_detail", pk=form.instance.pk)
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
