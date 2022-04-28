from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.music.models import Collection, Song
from apps.music.serializers import CollectionSerializer, SongSerializer


class CollectionCreateView(generics.CreateAPIView):
    queryset = Collection.genres.all()
    serializer_class = CollectionSerializer
    permission_classes = (IsAuthenticated,)


class CollectionEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collection.genres.all()
    serializer_class = CollectionSerializer
    permission_classes = (IsAuthenticated,)


class SongCreateView(generics.CreateAPIView):
    queryset = Song.tracks.all()
    serializer_class = SongSerializer
    permission_classes = (IsAuthenticated,)


class SongListView(generics.ListAPIView):
    queryset = Song.tracks.all()
    serializer_class = SongSerializer
    permission_classes = (IsAuthenticated,)


class SongEditView(generics.RetrieveUpdateAPIView):
    queryset = Song.tracks.all()
    serializer_class = SongSerializer
    permission_classes = (IsAuthenticated,)


class SongDeleteView(generics.DestroyAPIView):
    queryset = Song.tracks.all()
    serializer_class = SongSerializer
    permission_classes = (IsAuthenticated,)
