from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import IndexView, AuditoriumView


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('auditorium/', AuditoriumView.as_view(), name="auditorium"),
]


if settings.DEBUG == "True":
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
