from rest_framework import viewsets
from apps.landing_constructor.models import Tag as TagModel
from apps.landing_constructor.api.Serializers import TagSerializer
from django_filters.rest_framework import DjangoFilterBackend

class TagViewSet(viewsets.ModelViewSet):
    queryset = TagModel.objects.all()
    serializer_class = TagSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['parent', 'id']