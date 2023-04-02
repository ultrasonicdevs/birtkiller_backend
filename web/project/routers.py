from rest_framework.routers import DefaultRouter
from apps.landing_constructor.api.ViewSets import TagViewSet
from apps.landing_constructor.api.ViewSets import PageViewSet


router = DefaultRouter()
router.register('pages', PageViewSet)
router.register('tags', TagViewSet)
