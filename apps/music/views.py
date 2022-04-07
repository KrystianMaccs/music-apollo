from django.shortcuts import render
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from apps.music.models import Collection, Song
from apps.music.serializers import CollectionSerializer, SongSerializer


class CollectionCreateView(generics.CreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

class CollectionListView(generics.ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

class CollectionEditView(generics.RetrieveUpdateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

class CollectionDeleteView(generics.DestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class SongCreateView(generics.CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongListView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongEditView(generics.RetrieveUpdateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDeleteView(generics.DestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer