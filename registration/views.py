from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy

from .forms import SignUpForm, activate_user


class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("email_confirmation")


class UserActivationView(TemplateView):
    template_name = "registration/user_activation.html"

    def get(self, request, uidb64, token, *args, **kwargs):
        # Check user token
        result = activate_user(uidb64, token)
        # Pass boolean result to context
        return super().get(request, result=result, **kwargs)


class EmailConfirmationView(TemplateView):
    template_name = "registration/email_confirmation.html"
