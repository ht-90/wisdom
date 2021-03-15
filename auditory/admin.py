from django.contrib import admin

from . import models


@admin.register(models.Audio)
class AudioAdmin(admin.ModelAdmin):
    pass
