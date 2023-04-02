from django.db import models


class Tag(models.Model):
    tagname = models.CharField(max_length=128)
    component_type = models.CharField(max_length=128)
    parent = models.ForeignKey('self', related_name='children' , blank=True, null=True, on_delete=models.CASCADE)
    style_string = models.JSONField(blank=True)
    otherprops_string = models.JSONField(blank=True)
