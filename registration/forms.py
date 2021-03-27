from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.conf import settings

from django.http import request


from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator


User = get_user_model()


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        # Initialize user creation form
        user = super().save(commit=False)
        # Get submitted email
        user.email = self.cleaned_data["email"]
        # Set user inactive till email confirmation
        user.is_active = False

        if commit:
            user.save()
            activate_url = get_activate_url(user)
            message = settings.SIGNUP_MESSAGE_TEMPLATE + activate_url
            user.email_user(
                settings.SIGNUP_EMAIL_SUBJECT,
                message,
            )

        return user

def get_activate_url(user):
    # Encode username and generate token
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)

    return settings.FRONTEND_URL + "/activate/{}/{}/".format(uid, token)

def activate_user(uidb64, token):
    # Find user in database
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except Exception:
        return False

    # Activate user if token matches
    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return True

    return False
