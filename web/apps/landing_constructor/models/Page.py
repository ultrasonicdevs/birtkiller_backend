from django.db import models


class Page(models.Model):
    title = models.TextField()
    url = models.SlugField()
    objects = models.Manager()
