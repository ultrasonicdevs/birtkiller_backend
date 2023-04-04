from django.db import models
from . import Page


class Tag(models.Model):
    tagname = models.CharField(max_length=128)
    component_type = models.CharField(max_length=128)
    parent = models.ForeignKey('self', related_name='children', null=True, on_delete=models.CASCADE)
    style = models.JSONField(blank=True, null=True)
    other_props = models.JSONField(blank=True, null=True)
    page = models.ForeignKey(Page, blank=False, null=False, related_name='tags', on_delete=models.CASCADE)
