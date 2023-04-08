from django.contrib import admin
from django.urls import path, include, re_path
from project.routers import router
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


schema_view = get_schema_view(
   openapi.Info(
      title="Birtkiller API",
      default_version='v1',
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path(
        'admin/', 
        admin.site.urls
    ),
    path(
        'api/', 
        include(router.urls)
    ),
    re_path(r'^api/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^api/swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^api/redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/docs/', include_docs_urls(title='Birtkiller API'), name='schema-drf'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
