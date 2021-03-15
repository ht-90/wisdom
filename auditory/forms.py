from django import forms

from .models import Audio


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ["name", "audiofile"]
