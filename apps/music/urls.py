from django.urls import path
from apps.music.views import CollectionCreateView

urlpatterns = [
    path('list', CollectionCreateView.as_view()),
    #path('<pk:id>', SongCreateView.as_view()),
]