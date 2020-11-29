from rest_framework import serializers
from users.models import Profile, LanguageWithScore
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    """for projects you can use list seperator if more than one"""
    username = serializers.ReadOnlyField(source='user.username')
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')
    email = serializers.ReadOnlyField(source='user.email')
    languages = serializers.StringRelatedField(many=True,  allow_null=True)

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
            'languages',
            'cv',
            'academic_qualification',
            'academic_qualification_file',
            'projects'
        ]


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageWithScore
        fields = [
            'name',
            'score',
        ]