from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('create_announcement', views.create_announcement, name='create_announcement'),
    path('announcement_detail/<int:pk>', login_required(views.AnnouncementDetailView.as_view()),
         name='announcement_detail'),
    path('view_all_announcements', views.view_all_announcements, name='view_all_announcements'),
    path('create_comment/<int:pk>', views.create_comment, name='create_comment'),
    path('create_admin_comment/<int:id>', views.create_admin_comment, name='create_admin_comment'),
]
