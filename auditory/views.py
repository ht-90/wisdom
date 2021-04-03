from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView

from .models import Audio
from .forms import UploadFileForm


class HomeView(ListView):
    template_name = "home.html"
    model = Audio


class AuditoriumView(ListView):
    template_name = "auditorium.html"
    model = Audio


def audio_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UploadFileForm()

    # returns form to template
    return render(
        request,
        'upload.html',
        {'form': form}
    )


def success(request):
    return HttpResponse('successfully uploaded')
