from django.test import TestCase

from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

from ..forms import SignUpForm, get_activate_url, activate_user


class TestSignUpForm(TestCase):

    def test_valid_signup(self):
        """Ensure form validation"""
        data = {
            "username": "testuser",
            "email": "test@test.com",
            "password1": "testpass000",
            "password2": "testpass000",
        }
        form = SignUpForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_email(self):
        """Ensure form invalidation"""
        data = {
            "username": "testuser",
            "email": "test.com",
            "password1": "testpass000",
            "password2": "testpass000",
        }
        form = SignUpForm(data=data)
        self.assertFalse(form.is_valid(), "Email does not contain @.")

    def test_invalid_password(self):
        """Ensure form invalidation"""
        data = {
            "username": "testuser",
            "email": "test@test.com",
            "password1": "password",
            "password2": "password",
        }
        form = SignUpForm(data=data)
        self.assertFalse(form.is_valid(), "Password too common.")


class TestGetActivateUrl(TestCase):

    def setUp(self):
        """Setup a test user yet activated"""
        User = get_user_model()
        self.user = User()

    def test_get_activate_url(self):
        """Test generating a valid user activation url"""
        activate_url = get_activate_url(self.user)
        url_parts = activate_url.split("/")
        # assert correct url components
        self.assertEqual(len(url_parts), 7)
        # assert user id is not empty
        self.assertTrue(len(url_parts[-3]) > 0)
        # assert token is not empty
        self.assertTrue(len(url_parts[-2]) > 0)


class TestActivateUser(TestCase):

    def setUp(self):
        """Setup a test user"""
        User = get_user_model()
        user = User(id=1)
        User.objects.create(pk=user.pk)
        self.user = user

    def test_activate_user(self):
        """Test activating user"""
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        token = default_token_generator.make_token(self.user)
        # assert user activation
        self.assertTrue(activate_user(uidb64=uid, token=token))
        # assert user status is active
        self.assertTrue(self.user.is_active)
