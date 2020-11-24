from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.models import Token

from .managers import CustomUserManager


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """every user to have an automatically generated Token"""
    if created:
        Token.objects.create(user=instance)

class CustomUser(AbstractUser):
    """New class called CustomUser that subclasses AbstractUser and removed the username field"""

    # Part of AbstractUser
    # first_name
    # last_name
    # date_joined

    email = models.EmailField(_('email address'), unique=True)
    favourite_language = models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length=200, blank=True,
                           verbose_name="Biography")

    github_url = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True,blank=True)
    cv = models.FileField(_("Upload your CV"), upload_to="CV", max_length=100, blank=True)
    bachelor_degree = models.CharField(_("Enter your bachelors degree"), max_length=30, blank=True)
    masters_degree = models.CharField(_("Enter your master's degree"), max_length=30, blank=True)


    # remove username and use email as the unique identifier
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_profile_picture(self):
        if self.profile_picture != '':
            return True
        return False
