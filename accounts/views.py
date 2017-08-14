from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "accounts/index.html")


def complainant(request):
    return render(request, "accounts/complainant.html")


def clogin(request):
    return render(request, "accounts/login.html")
