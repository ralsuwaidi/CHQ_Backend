from django.contrib.auth.models import User
from rest_framework import generics, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from users.models import Profile, LanguageWithScore
from users.permissions import IsOwnerOrReadOnly
from users.serializers import ProfileSerializer, LanguageWithScore


class ProfileList(mixins.ListModelMixin,
                  generics.GenericAPIView):
    """
    List all snippets, or create a new profile.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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
            profile = Profile.objects.get(id=user.id)
        except:
            # ceate new profile for the user
            profile = Profile(id=user.id, user=user)

        # May raise a permission denied
        self.check_object_permissions(self.request, profile)

        return profile

    # def put(self, request,username, format=None):
    #     profile = self.get_object()
    #     print(request.data)

    #     serializer = ProfileSerializer(profile, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'profiles': reverse('profile-list', request=request, format=format)
    })

