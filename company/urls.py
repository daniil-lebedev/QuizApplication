from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.homa_page, name="home_page"),
]
