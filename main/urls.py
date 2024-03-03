from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static

from main import settings

schema_view = get_schema_view(
    openapi.Info(
        title="TestApp",
        default_version='v1',
        description="Swagger",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny,]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/news/', include('news.urls')),
    path('api/v1/courses/', include('courses.urls')),
    path('api/v1/tests/', include('my_tests.urls')),
    path('api/v1/videos/', include('videos.urls')),
    path('api/v1/questions/', include('questions.urls')),
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

