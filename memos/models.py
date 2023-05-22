from django.db import models
from django.utils import timezone


class Memo(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now)
