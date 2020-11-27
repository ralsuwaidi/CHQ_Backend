from django.db import models

class Profile(models.Model):
    github_url = models.URLField(null=True)
    bio = models.TextField(blank=True)
    username = models.ForeignKey('auth.User', related_name='profile',on_delete=models.CASCADE)

