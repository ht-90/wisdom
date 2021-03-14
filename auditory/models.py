from django.db import models
import uuid

from .validators import validate_file_extension, validate_file_size


class Audio(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(max_length=50) 
    audiofile = models.FileField(
        upload_to='',
        validators=[
            validate_file_extension,
            validate_file_size,
        ]
    )
