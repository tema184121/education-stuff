from django.contrib import admin

from videos.models import VideoClip


@admin.register(VideoClip)
class VideoClipAdmin(admin.ModelAdmin):
    pass
