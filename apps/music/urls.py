from django.urls import path

from .views import *

urlpatterns = [
    path("create-collection", CollectionListView.as_view()),
    path("<int:user>", CollectionEditView.as_view()),
    path("create-song", SongCreateView.as_view()),
    path("<int:user>", SongEditView.as_view()),
]
