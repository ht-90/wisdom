from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import IndexView, AuditoriumView, audio_upload, success


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('auditorium/', AuditoriumView.as_view(), name="auditorium"),
    path('upload/', audio_upload, name='upload'),  # if function is used rather than view object, a new url page is created without template file
    path('success/', success, name='success'),
]


if settings.DEBUG == "True":
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
