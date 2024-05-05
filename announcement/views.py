from types import NoneType

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView

from company.models import Team, TeamAdmin
from .forms import CreateAnnouncementForm, CreateComment, CreateAdminCommentForm
from .models import Announcement, AdminComment, Comment


# Create your views here.
@login_required
@login_required
def announcement_detail(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    member_comments = Comment.objects.filter(announcement=announcement).order_by('-created_at')
    admin_comments = AdminComment.objects.filter(announcement=announcement).order_by('-created_at')

    context = {
        'announcement': announcement,
        'member_comments': member_comments,
        'admin_comments': admin_comments,
    }
    return render(request, 'announcement/view_announcement.html', context)


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
    # get all announcements from teams that user is a member of
    announcements = Announcement.objects.filter(team__team_of_member__user=request.user).order_by('-created_at')
    return render(request, "announcement/view_all_announcements.html", {"announcements": announcements})


@login_required
def create_comment(request, pk) -> render:
    """
    Allows a user to create a comment.
    :param request:
    :param pk: The primary key of the announcement.
    :return: render
    """
    form = CreateComment()
    announcement = Announcement.objects.get(pk=pk)
    if request.method == "POST":
        try:
            form = CreateComment(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.announcement = announcement
                comment.created_by = request.user.team_member.first()
                form.save()
                return redirect("announcement_detail", pk=pk)
        except NoneType:
            messages.warning(request, "An error occurred while creating the comment!")
            return redirect("create_comment", pk=pk)
    return render(request, "announcement/create_comment.html", {"form": form})


@login_required
def create_admin_comment(request, announcement_id):
    announcement = get_object_or_404(Announcement, pk=announcement_id)
    team = announcement.quiz.belongs_to  # Assuming 'quiz' has a 'belongs_to' field pointing to 'Team'

    # Check if the current user is allowed to view the team as an admin
    if not TeamAdmin.objects.filter(user=request.user, team=team).exists():
        messages.error(request, "You are not authorized to comment as an admin on this announcement.")
        return redirect('announcement_detail', pk=announcement_id)

    if request.method == "POST":
        form = CreateAdminCommentForm(request.POST)
        try:
            if form.is_valid():
                comment = form.save(commit=False)
                comment.announcement = announcement
                comment.created_by = TeamAdmin.objects.get(user=request.user, team=team)
                if not comment.created_by:
                    messages.error(request, "You are not a registered team admin.")
                    return render(request, "announcement/create_comment.html", {"form": form})
                comment.save()
                messages.success(request, "Comment created successfully")
                return redirect("announcement_detail", pk=announcement_id)
        except NoneType:
            messages.error(request, f"An error occurred while creating the comment!")
            return redirect("create_admin_comment", announcement_id)
    else:
        form = CreateAdminCommentForm()

    return render(request, "announcement/create_comment.html", {"form": form})


@login_required
def delete_admin_comment(request, comment_id):
    comment = get_object_or_404(AdminComment, id=comment_id)

    # Check if the user is allowed to delete the comment
    if comment.created_by.user != request.user:
        messages.error(request, "You do not have permission to delete this comment.")
        return redirect('announcement_detail', comment.announcement.id)

    if request.method == 'POST':
        comment.delete()
        messages.success(request, "Admin comment deleted successfully.")
        return redirect('announcement_detail', comment.announcement.id)

    return render(request, 'announcement/comment_confirm_delete.html', {'comment': comment})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Check if the user is the creator of the comment or an admin
    if comment.created_by.user != request.user:
        messages.error(request, "You do not have permission to delete this comment.")
        return redirect('announcement_detail', comment.announcement.id)

    if request.method == 'POST':
        comment.delete()
        messages.success(request, "Comment deleted successfully.")
        return redirect('announcement_detail', comment.announcement.id)

    return render(request, 'announcement/comment_confirm_delete.html', {'comment': comment})
