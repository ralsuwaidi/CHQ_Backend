import time

import requests
from django.contrib.auth.models import User
from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
import urllib, json
from users.exceptions import CannotCreateSameLanguage, ProfileNotCreated
from users.models import Hackathon, LanguageWithScore, Profile
from users.permissions import IsOwnerOrReadOnly
from users.serializers import (HackathonSerializer, LanguageSerializer,
                               ProfileSerializer)


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
        print(user)

        try:
            # get profile of user has a profile
            profile = Profile.objects.get(id=user.id)
        except:
            # ceate new profile for the user
            profile = Profile(id=user.id, user=user)
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
    url = "https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fblog.codinghorror.com%2Frss%2F"
    response = urllib.request.urlopen(url)

    data = json.loads(response.read())
    return Response(data=data)


@api_view(['POST', 'GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def add_language(request, username):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        serializer = LanguageSerializer(data=request.data)
        if serializer.is_valid():
            user = get_object_or_404(User.objects.all(), username=username)

            # check if profile exists
            try:
                profile = Profile.objects.get(user=user.id)
            except:
                raise ProfileNotCreated

            # same language cannot be added twice
            languages = LanguageWithScore.objects.all()
            if languages.filter(name=request.data['name']).exists():
                raise CannotCreateSameLanguage

            # save to db
            serializer.save(profile=profile)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        # get all languages related to user
        user = get_object_or_404(User.objects.all(), username=username)
        lang = LanguageWithScore.objects.filter(profile=user.pk)
        serializer = LanguageSerializer(lang, many=True)
        return Response(serializer.data)


class HackathonViewset(viewsets.ModelViewSet):
    """many to many relationship
    https://medium.com/@kingsleytorlowei/building-a-many-to-many-modelled-rest-api-with-django-rest-framework-d41f54fe372
    """
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer


@api_view(['GET', ])
def external_api_view(request, id=None):
    attempt_num = 0  # keep track of how many times we've retried
    while attempt_num < 5:
        if id is None:
            r = requests.get(
                "https://hacker-news.firebaseio.com/v0/topstories.json", timeout=10)
        else:
            r = requests.get(
                "https://hacker-news.firebaseio.com/v0/item/{}.json?".format(id), timeout=10)
        if r.status_code == 200:
            data = r.json()
            return Response(data, status=status.HTTP_200_OK)
        else:
            attempt_num += 1
            # You can probably use a logger to log the error here
            time.sleep(5)  # Wait for 5 seconds before re-trying
    return Response({"error": "Request failed"}, status=r.status_code)
