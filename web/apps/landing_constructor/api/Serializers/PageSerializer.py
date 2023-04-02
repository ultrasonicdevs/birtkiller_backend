from rest_framework import serializers
from ...models import Page as PageModel


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageModel
        fields = '__all__'