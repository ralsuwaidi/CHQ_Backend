from django.http import HttpResponse
from django.shortcuts import render, redirect,reverse
from users.forms import CustomUserCreationForm
from django.contrib.auth import login


def index(request):
    return HttpResponse("You're looking at the index page")


def profile(request):
    return render(request, "users/profile.html")


def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("users:profile"))
