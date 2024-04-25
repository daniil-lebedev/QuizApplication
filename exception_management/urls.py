from django.urls import path

from .views import *

urlpatterns = [
    path("error_404", error_404, name="error_404"),
    path("error_500", error_500, name="error_500"),
    path("error_403", error_403, name="error_403"),
    path("error_400", error_400, name="error_400"),
]
