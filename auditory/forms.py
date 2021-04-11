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
widget_thumbnail = forms.ClearableFileInput(attrs={'class': 'mb-5'})
widget_audiofile = forms.ClearableFileInput(attrs={'class': 'mb-5'})
widget_author = forms.TextInput(attrs={
    "class": "input is-info mb-5",
    "placeholder": "Author",
})


class UploadFileForm(forms.ModelForm):
    """File upload form with custom styling"""
    name = forms.CharField(label="", widget=widget_name)
    description = forms.CharField(label="", widget=widget_description)
    author = forms.CharField(label="", widget=widget_author)

    class Meta:
        model = Audio
        fields = ("name", "description", "thumbnail", "audiofile", "author")
        widgets = {
            "thumbnail": widget_thumbnail,
            "audiofile": widget_audiofile,
        }
