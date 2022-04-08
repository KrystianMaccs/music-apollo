from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from apps.music.models import Collection, Song
from apps.music.serializers import CollectionSerializer, SongSerializer


class CollectionCreateView(generics.CreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = (IsAuthenticated,)

class CollectionListView(generics.ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = (IsAuthenticated,)

class CollectionEditView(generics.RetrieveUpdateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = (IsAuthenticated,)

class CollectionDeleteView(generics.DestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = (IsAuthenticated,)


class SongCreateView(generics.CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = (IsAuthenticated,)

class SongListView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = (IsAuthenticated,)

class SongEditView(generics.RetrieveUpdateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = (IsAuthenticated,)

class SongDeleteView(generics.DestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = (IsAuthenticated,)