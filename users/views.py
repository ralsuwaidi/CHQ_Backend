from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from users.forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth import login
from rest_framework import viewsets          # add this
from .serializers import CustomUserSerializer      # add this
from .models import CustomUser                     # add this

class CustomUserView(viewsets.ModelViewSet):       # add this
    serializer_class = CustomUserSerializer          # add this
    queryset = CustomUser.objects.all()              # add this


def index(request):
    return HttpResponse("You're looking at the index page")


def profile(request):
    if request.method == "GET":
        return render(
            request, "users/profile.html",
            {"form": ProfileForm}
        )
    elif request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user) 
        if form.is_valid():
            user=form.save()
            print(user.has_profile_picture())
            # login(request, user)
            return redirect(reverse("users:profile"))


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
