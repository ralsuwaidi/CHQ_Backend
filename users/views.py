import json
import time
import urllib

import requests
from django.contrib.auth.models import User
from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse

import users.news as news
import users.exceptions as CustomExceptions
from users.models import Hackathon, Profile
from users.permissions import IsOwnerOrReadOnly
from users.serializers import (HackathonSerializer,
                               ProfileSerializer)

from users import news


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'username'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get_object(self):
        """
        Returns the object the view is displaying.

        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        user = get_object_or_404(queryset, **filter_kwargs)

        try:
            # get profile of user has a profile
            profile = Profile.objects.get(user=user)
        except:
            # ceate new profile for the user
            profile = Profile(user=user)
            profile.full_clean()
            profile.save()

        # May raise a permission denied
        self.check_object_permissions(self.request, profile)

        return profile


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'profiles': reverse('profile-list', request=request, format=format)
    })

@api_view(['GET'])
def index(request):
    """default root directory will show news as json"""
    data = news.show_news(news.DEFAULT_NEWS)
    return Response(data=data)

@api_view(['GET'])
def profile_news(request, username):
    """get current user's prefered news source as json"""

    user = get_object_or_404(User.objects.all(), username=username)
    # check if profile exists
    try:
        profile = Profile.objects.get(user=user.id)
    except:
        raise CustomExceptions.ProfileNotCreated

    # check if prefered news exists within saved news
    news_pref = profile.news_pref

    data = None
    if news_pref=="":
        data = news.show_news(news.DEFAULT_NEWS)
    else:
        if news_pref not in news.NEWS_SITES:
            raise CustomExceptions.NewsSourceNotAvailable
        data = news.show_news(profile.news_pref)
    return Response(data=data)


class HackathonViewset(viewsets.ModelViewSet):
    """many to many relationship
    https://medium.com/@kingsleytorlowei/building-a-many-to-many-modelled-rest-api-with-django-rest-framework-d41f54fe372
    """
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer


