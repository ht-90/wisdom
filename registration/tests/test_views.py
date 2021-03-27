from django.test import TestCase, Client

from ..models import User


class TestSignUpView(TestCase):
    def setUp(self):
        self.user_data = {
            "username": "testuser",
            "email": "test@test.com",
            "password1": "testpass000",
            "password2": "testpass000",
        }

    def test_request_signup(self):
        """Test request user sign up"""
        c = Client()
        c.post("/signup/", self.user_data)
        user = User.objects.get(username="testuser")
        self.assertTrue(user.username, "username")

    def test_user_not_active(self):
        """Test user is not active when form submitted"""
        c = Client()
        c.post("/signup/", self.user_data)
        user = User.objects.get(username="testuser")
        self.assertFalse(user.is_active, "User email hasn't been confirmed.")
