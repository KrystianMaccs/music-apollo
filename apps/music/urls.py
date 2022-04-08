from django.urls import path
from .views import *

urlpatterns = [
    path('create-collection', CollectionCreateView.as_view()),
    path('create-collection/list-collection', CollectionListView.as_view()),
    path('<int:pk>', CollectionEditView.as_view()),
    path('<int:pk>/delete', CollectionDeleteView.as_view()),
    path('create-song', SongCreateView.as_view()),
    path('create-song/song-list', SongListView.as_view()),
    path('<int:pk>', SongEditView.as_view()),
    path('<int:pk>/delete', SongDeleteView.as_view()),
]