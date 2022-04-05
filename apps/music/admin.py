from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin

from apps.music.models import Collection, Song

admin.site.register((Collection, Song))
