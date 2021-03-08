import logging

from django.db import models

import requests

logger = logging.getLogger(__name__)

# Create your models here.
class Song(models.Model):
    artist = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    lyrics = models.CharField(max_length=10000)

    class Meta:
        managed = False

    def __init__(self, artist, title):
        self.artist = artist
        self.title = title
        response = requests.get('https://api.lyrics.ovh/v1/' + artist + '/' + title)
        logger.debug(response)
        self.lyrics = response.json()['lyrics']