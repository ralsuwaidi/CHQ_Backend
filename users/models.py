from .managers import CustomUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser

from django.db import models


class CustomUser(AbstractUser):
    """New class called CustomUser that subclasses AbstractUser and removed the username field"""

    email = models.EmailField(_('email address'), unique=True)
    favourite_language = models.CharField(max_length=30,blank=True)

    # remove username and use email as the unique identifier
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
