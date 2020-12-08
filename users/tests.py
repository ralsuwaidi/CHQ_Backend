from django.test import TestCase
from users.models import Profile
from django.contrib.auth.models import User
# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        user = User()
        user.username="test_ssuser"
        user.set_password("mynewPASS33")
        user.email="testEmail@email.com"
        user.save()

    def test_user_creation(self):
        """Animals that can speak are correctly identified"""
        user = User.objects.get(username="test_ssuser")
        self.assertEqual(user.email, "testEmail@email.com", msg="Grabbed user has a different email")
        self.assertEqual(user.check_password("mynewPASS33"), True)

    def test_user_change_password(self):
        user = User.objects.get(username="test_ssuser")
        user.set_password("userNEWpass")
        self.assertEqual(user.check_password("userNEWpass"), True)

    def test_user_profile_default_score(self):
        user = User.objects.get(username="test_ssuser")
        profile = Profile(id=user.id, user=user)
        profile.save()
        user_profile = Profile.objects.get(id=user.id)
        self.assertEqual(user_profile.back_end_score, 20)
        self.assertEqual(user_profile.front_end_score, 20)

        