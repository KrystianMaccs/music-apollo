from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.users.urls")),
    path("music/", include("apps.music.urls")),
]

admin.site.site_header = "Apollo Admin"
admin.site.site_title = "Apollo Admin Portal"
admin.site.index_title = "Welcome to the Apollo Portal"