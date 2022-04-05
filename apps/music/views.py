from django.shortcuts import render
from rest_framework import generics
from apps.music.models import Collection, Song
from apps.music.serializers import CollectionSerializer, SongSerializer


class CollectionCreateView(generics.CreateAPIView):
    model = Collection
    serializer_class = CollectionSerializer


"""class SongCreateView(generics.CreateAPIView):
    model = Song
    serializer_class = SongSerializer"""