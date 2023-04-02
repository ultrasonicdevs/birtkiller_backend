from rest_framework import viewsets
from apps.landing_constructor.models import Page as PageModel
from apps.landing_constructor.api.Serializers import PageSerializer

class PageViewSet(viewsets.ModelViewSet):
    queryset = PageModel.objects.all()
    serializer_class = PageSerializer