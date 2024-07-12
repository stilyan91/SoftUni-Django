from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=False)
