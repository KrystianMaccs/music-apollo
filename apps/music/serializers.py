from rest_framework import serializers

from apps.music.models import Collection, Song


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "user", "genre"]


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["id", "track", "title", "collection", "artiste", "artwork"]
