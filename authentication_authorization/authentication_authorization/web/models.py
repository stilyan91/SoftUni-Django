from django.db import models

class Article(models.Model):
    create_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, null=False, blank=False)