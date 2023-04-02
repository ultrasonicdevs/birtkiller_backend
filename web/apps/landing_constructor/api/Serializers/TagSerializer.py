from rest_framework import serializers
from ...models import Tag as TagModel



class ChildTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagModel
        exclude = ('parent',)

class TagSerializer(serializers.ModelSerializer):
    tag_set = ChildTagSerializer(many=True, source='children')
    class Meta:
        model = TagModel
        fields = '__all__'

