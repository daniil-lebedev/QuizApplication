from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the polls index.")


def view_to_create_company(request) -> HttpResponse:
    return HttpResponse("This is the view to create a company.")
