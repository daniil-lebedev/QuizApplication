from django.urls import path

from .views import base, index

urlpatterns = [
    path('', index, name='index'),
    path('base', base, name='landing_page'),
]
