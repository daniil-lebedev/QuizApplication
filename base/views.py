from django.shortcuts import render


# Create your views here.

def base(request) -> render:
    return render(request, "base/base.html")


def index(request) -> render:
    return render(request, "base/index.html")
