from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import redirect, render, reverse
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.forms import CustomUserCreationForm, ProfileForm

from .models import CustomUser
from .serializers import CustomUserSerializer, RegistrationSerializer


class CustomUserView(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

# resitrict to post request
@api_view(['POST',])
def register(request):
    serializer = RegistrationSerializer(data=request.data)
    print(request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        data['response'] = "successfully registered a new user."
        data['email'] = user.email
    else:
        data = serializer.errors
    return Response(data)



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
            user = form.save()
            print(user.has_profile_picture())
            # login(request, user)
            return redirect(reverse("users:profile"))


# def register(request):
#     if request.method == "GET":
#         return render(
#             request, "users/register.html",
#             {"form": CustomUserCreationForm}
#         )
#     elif request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect(reverse("users:profile"))
