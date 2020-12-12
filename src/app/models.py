from django.db import models

from behaviors.behaviors import Timestamped


class DefaultModel(models.Model):
    class Meta:
        abstract = True


class TimestampedModel(DefaultModel, Timestamped):
    class Meta:
        abstract = True
