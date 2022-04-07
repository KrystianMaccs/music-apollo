from django.conf import settings
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf.urls import url


schema_view = get_schema_view(
   openapi.Info(
      title="Apollo",
      default_version='v1',
      description="Apollo: A music storage app",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="krystianmaccs@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    url('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path("", include("apps.users.urls")),
    path("music/", include("apps.music.urls")),
]

admin.site.site_header = "Apollo Admin"
admin.site.site_title = "Apollo Admin Portal"
admin.site.index_title = "Welcome to the Apollo Portal"