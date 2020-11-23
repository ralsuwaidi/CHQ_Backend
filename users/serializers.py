from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ('email',
    'favourite_language',
    'bio',
    'github_url',
    'bachelor_degree',
    'masters_degree'
    )