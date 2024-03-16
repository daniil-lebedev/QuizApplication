from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register_user, name="register_user"),
    path("profile", views.user_profile, name="user_profile"),
    path("login", views.login_user, name="login_user"),
]
