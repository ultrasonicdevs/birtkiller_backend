from rest_framework import serializers
from ...models import Tag as TagModel
from rest_framework_recursive.fields import RecursiveField


class TagSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True, required=False)
    class Meta:
        model = TagModel
        fields = '__all__'
