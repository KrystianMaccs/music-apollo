from rest_framework import serializers

from apps.music.models import Collection, Song


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["user", "genre"]


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["track", "title", "collection", "artiste", "artwork"]
