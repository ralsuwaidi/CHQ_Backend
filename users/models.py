from django.db import models


class RateSelf(models.Model):
    FRONTEND = 'FE'
    BACKEND = 'BE'
    DATABASE = 'DA'
    DEVOPS = 'DO'
    MOBILE = 'MO'
    CRITERIA_CHOICES = [
        (FRONTEND, 'Frontend'),
        (BACKEND, 'Backend'),
        (DATABASE, 'Database'),
        (DEVOPS, 'Devops'),
        (MOBILE, 'Mobile'),
    ]
    Criteria = models.CharField(
        max_length=2,
        choices=CRITERIA_CHOICES,
    )

    
class Profile(models.Model):
    github_url = models.URLField(null=True)
    bio = models.TextField(blank=True)
    username = models.ForeignKey('auth.User', related_name='profile',on_delete=models.CASCADE)