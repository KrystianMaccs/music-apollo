from django.db import models
from apps.commons.models import TimeStampedUUIDModel

from django.contrib.auth import get_user_model

User = get_user_model()

class Collection(TimeStampedUUIDModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT, max_length=50)
    genre = models.CharField(max_length=120, blank=False, null=False)

    def __str__(self):
        return self.genre

class Song(TimeStampedUUIDModel):
    track = models.FileField(upload_to="mediafiles/", null=False, blank=False, default=True)
    title = models.CharField(max_length=120, blank=False, null=False)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    artiste = models.CharField(max_length=50, null=False, blank=False, default=True)
    artwork = models.ImageField(upload_to="staticfiles/", blank=True, default=True)


    def __str__(self):
        return self.title



