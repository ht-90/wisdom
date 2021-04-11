from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import uuid
import mutagen

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
    description = models.CharField(
        max_length=200,
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
    author = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        default="Not Available",
    )
    duration = models.IntegerField(
        blank=True,
        null=True,
        default=1
    )
    uploaded = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=False,
        null=True,
    )

    def __str__(self):
        return self.name


@receiver(pre_save, sender=Audio)
def audio_duration_reader(sender, instance, **kwargs):
    """Update auido duration value before saving audio object"""
    try:
        # Read audio file metadata
        audio_info = mutagen.File(instance.audiofile).info

        # Update audio duration field value
        instance.duration = int(audio_info.length)

    except Exception as e:
        print(e)


@receiver(post_delete, sender=Audio)
def audio_post_delete_handler(sender, **kwargs):
    """Delete audio and thumbnail files on object deletion"""
    # Get Audio instance
    audio = kwargs["instance"]

    # Get path and name of audio and thumbnail files
    audio_storage, audio_name = audio.audiofile.storage, audio.audiofile.name
    thumbnail_storage, thumbnail_name = audio.thumbnail.storage, audio.thumbnail.name

    # Delete files in storage
    audio_storage.delete(audio_name)
    thumbnail_storage.delete(thumbnail_name)
