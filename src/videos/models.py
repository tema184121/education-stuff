from django.db import models
from django.utils.translation import gettext_lazy as _

from app.models import TimestampedModel


class VideoClip(models.Model):
    channel = models.ForeignKey(
        'channels.Channel', verbose_name=_('Parent channel'),
        on_delete=models.DO_NOTHING,
    )

    title = models.CharField(_('Clip title'), max_length=128)
    description = models.TextField()
    views_count = models.PositiveIntegerField()

    file = models.FileField()
