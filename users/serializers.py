from rest_framework import serializers
from users.models import Profile, LanguageWithScore
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')
    email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Profile
        fields = [
            'github_url',
            'bio',
            'username',
            'first_name',
            'last_name',
            'email',
            'mobile_score',
            'devops_score',
            'front_end_score',
            'back_end_score',
            'database_score',
        ]


