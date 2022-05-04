from django.contrib.auth import get_user_model
from django.db import models

from apps.commons.models import TimeStampedUUIDModel

User = get_user_model()


class CollectionQuerySet(models.QuerySet):
    def genre(self):
        return self.filter(int=user).order_by("-created")


class PopularCollectionManager(models.Manager):
    def get_queryset(self):
        return CollectionQuerySet(self.model, using=self._db)


class Collection(TimeStampedUUIDModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT, max_length=50)
    genre = models.CharField(max_length=120, blank=False, null=False)

    genres = PopularCollectionManager()

    def __str__(self):
        return self.genre


class SongQuerySet(models.QuerySet):
    def genre(self):
        return self.filter(user=user).order_by("-created")


class TopSongManager(models.Manager):
    def get_queryset(self):
        return SongQuerySet(self.model, using=self._db)


class Song(TimeStampedUUIDModel):
    track = models.FileField(
        upload_to="mediafiles/", null=False, blank=False, default=True
    )
    title = models.CharField(max_length=120, blank=False, null=False)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    artiste = models.CharField(
        max_length=50, null=False, blank=False, default="Juice WRLD"
    )
    artwork = models.ImageField(upload_to="staticfiles/", blank=True, default=True)

    tracks = TopSongManager()

    def __str__(self):
        return self.title
