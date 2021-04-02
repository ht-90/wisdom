"""wisdom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.decorators import login_required

from registration.views import SignUpView, UserActivationView
from auditory.views import HomeView, audio_upload, success, AuditoriumView

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # Registration app
    path('', include("django.contrib.auth.urls")),
    path('', login_required(HomeView.as_view())),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('activate/<uidb64>/<token>/', UserActivationView.as_view(), name="activate"),
    # Auditory app
    path('home/', HomeView.as_view(), name="home"),
    path('upload/', audio_upload, name='upload'),
    path('success/', success, name='success'),
    path('auditorium/<str:id>', AuditoriumView.as_view(), name="auditorium"),
]

# Add media storage paths
if settings.DEBUG == "True":
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
