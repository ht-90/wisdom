from django.urls import path

from .views import IndexView, AuditoriumView


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('auditorium/', AuditoriumView.as_view(), name="auditorium"),
]
