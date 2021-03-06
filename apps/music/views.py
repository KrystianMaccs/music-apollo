from django.contrib.auth import get_user_model
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions

from apps.music.models import Collection, Song
from apps.music.serializers import CollectionSerializer, SongSerializer

User = get_user_model()
# from rest_framework.permissions import IsAuthenticated


class CollectionListView(generics.ListCreateAPIView):
    serializer_class = CollectionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        user = self.request.user
        return Collection.genres.filter(user=user).order_by("-created")


class CollectionEditView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CollectionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        user = self.request.user
        return Collection.genres.filter(user=user).order_by("-created")


class SongCreateView(generics.ListCreateAPIView):
    serializer_class = SongSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        user = self.request.user
        return Song.tracks.filter(user=user).order_by("-created")


class SongEditView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SongSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        user = self.request.user
        return Song.tracks.filter(user=user).order_by("-created")
