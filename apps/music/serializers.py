from rest_framework import serializers
from apps.music.models import Collection, Song

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = "__all__"

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"