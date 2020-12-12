from django.db import models
from django.utils.translation import gettext_lazy as _

from app.models import TimestampedModel


class Channel(TimestampedModel):
    owner = models.ForeignKey(
        'users.User', verbose_name=_('Channel owner'), on_delete=models.PROTECT, related_name='channels',
        related_query_name='channel',
    )

    title = models.CharField(_('Channel title'), max_length=50)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title
