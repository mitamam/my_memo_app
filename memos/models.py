from django.db import models


class Memo(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField()
