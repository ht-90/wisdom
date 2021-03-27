from django.test import TestCase

from ..models import User


class TestUser(TestCase):
    """Test User model for registration"""

    def setUp(self):
        User.objects.create(
            username="testuser",
            email="test@test.com",
            password="testpass000",
        )

    def test_user_fields(self):
        """Test User fields when created"""
        user = User.objects.get(username="testuser")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@test.com")
        self.assertEqual(user.password, "testpass000")

    def test_user_status(self):
        """Test User is active when User object is added"""
        user = User.objects.get(username="testuser")
        self.assertTrue(user.is_active)
