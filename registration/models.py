from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy


class User(AbstractUser):
    email = models.EmailField("email_address", unique=True)

    def get_absolute_url(self):
        return reverse_lazy("login")
