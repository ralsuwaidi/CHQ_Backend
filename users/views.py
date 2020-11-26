from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import redirect, render, reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from users.forms import CustomUserCreationForm, ProfileForm

from .models import CustomUser, Profile
from .serializers import UserSerializer, RegistrationSerializer, ProfileSerializer


# resitrict to post request
@api_view(['POST', ])
def register(request):
    """
    An endpoint for registering user
    email,password,password2
    """
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


class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class ProfileView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


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
