from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, "index.html")

def register(request):
    # placeholder for now - stoped where we reached..
    """
    if request.method == "POST":
        errors = User.objects.user_validator(request.POST)
        if errors:
            for key, msg in errors.items():
                messages.error(request, msg)
    """
    return redirect("success")

def login(request):
    return redirect("success")

def logout(request):
    return redirect("success")

def success(request):
    return render(request, "success.html")
