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

    def get_queryset(self):
        """Filter audio object by audio id"""
        return Audio.objects.filter(uuid=self.kwargs["id"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["other_audios"] = Audio.objects.exclude(uuid=self.kwargs["id"]).all()
        # Prevent passing over 10 audios
        if len(context["other_audios"]) > 10:
            context["other_audios"] = context["other_audios"][:10]
        return context


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
