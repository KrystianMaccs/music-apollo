from django.db import models
from apps.commons.models import TimeStampedUUIDModel

from django.contrib.auth import get_user_model

User = get_user_model()

class CollectionQuerySet(models.QuerySet):
    def genre(self):
        return self.annotate(genre=genre("name")).filter(genre__gte=10)

class PopularCollectionManager(models.Manager):
    def get_queryset(self):
        return CollectionQuerySet(self.model, using=self._db)

    def genre(self):
        return self.get_queryset().genre()


class Collection(TimeStampedUUIDModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT, max_length=50)
    genre = models.CharField(max_length=120, blank=False, null=False)

    genres = PopularCollectionManager()

    def __str__(self):
        return self.genre


class SongQuerySet(models.QuerySet):
    def genre(self):
        return self.annotate(genre=genre("name")).filter(track__gte=10)

class TopSongManager(models.Manager):
    def get_queryset(self):
        return SongQuerySet(self.model, using=self._db)

    def genre(self):
        return self.get_queryset().track()

class Song(TimeStampedUUIDModel):
    track = models.FileField(upload_to="mediafiles/", null=False, blank=False, default=True)
    title = models.CharField(max_length=120, blank=False, null=False)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    artiste = models.CharField(max_length=50, null=False, blank=False, default="Juice WRLD")
    artwork = models.ImageField(upload_to="staticfiles/", blank=True, default=True)

    tracks = TopSongManager()


    def __str__(self):
        return self.title




