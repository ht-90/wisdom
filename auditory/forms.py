from django import forms

from .models import Audio


# Custom design of form inputs
widget_name = forms.TextInput(attrs={
    "class": "input is-info mb-5",
    "placeholder": "Audio title"
})
widget_description = forms.Textarea(attrs={
    "class": "textarea is-info mb-5",
    "placeholder": "Description",
    "rows": 4
})
widget_thumbnail = forms.FileInput(attrs={
    "class": "mb-5",
    "type": "file"
})
widget_audiofile = forms.FileInput(attrs={
    "class": "mb-5"
})


class UploadFileForm(forms.ModelForm):
    """File upload form with custom styling"""
    name = forms.CharField(label="", widget=widget_name)
    description = forms.CharField(label="", widget=widget_description)
    thumbnail = forms.CharField(label="Thumbnail image file", widget=widget_thumbnail)
    audiofile = forms.CharField(label="Audio file", widget=widget_audiofile)

    class Meta:
        model = Audio
        fields = ("name", "description", "thumbnail", "audiofile")
