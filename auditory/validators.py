from django.core.exceptions import ValidationError

from django.conf import settings


def validate_file_extension(fileobj):
    ext = fileobj.name.split(".")[-1]
    if ext not in settings.ALLOWED_AUDIO_EXTENSIONS:
        raise ValidationError(f"""
        {ext} file format is not supported.
        Format must be one of [{", ".join(settings.ALLOWED_AUDIO_EXTENSIONS)}].
        """)


def validate_file_size(fileobj):
    if fileobj.size > settings.MAX_UPLOAD_SIZE:
        raise ValidationError(
            f"File size is too large. Max {settings.MAX_UPLOAD_SIZE} is allowed."
        )
