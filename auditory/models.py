from django.db import models
from django.conf import settings
import uuid

from .validators import validate_file_extension, validate_file_size


class Audio(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(
        max_length=50,
        blank=False,
        null=True,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    thumbnail = models.ImageField(
        upload_to="thumbnail",
        null=True,
    )
    audiofile = models.FileField(
        upload_to='audio',
        validators=[
            validate_file_extension,
            validate_file_size,
        ]
    )

    def __str__(self):
        return self.name
