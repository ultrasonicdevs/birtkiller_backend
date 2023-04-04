from rest_framework import serializers
from ...models import Page as PageModel
from ...models import Tag as TagModel
from .TagSerializer import TagSerializer


class PageSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    
    def get_tags(self, obj):
        return TagSerializer(TagModel.objects.filter(parent__isnull=True), many=True).data

    class Meta:
        model = PageModel
        fields = '__all__'