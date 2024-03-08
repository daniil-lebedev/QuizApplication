from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the polls index.")


def homa_page(request) -> HttpResponse:
    return render(request, "company/index.html")
