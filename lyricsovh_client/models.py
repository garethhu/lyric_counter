import logging

from django.db import models

import requests

logger = logging.getLogger(__name__)

# Create your models here.


class Song(models.Model):
    artist = models.CharField(max_length=100)  # TODO pull out length to config
    title = models.CharField(max_length=100)  # TODO pull out length to config
    lyrics = models.CharField(max_length=10000)  # TODO pull out length to config

    class Meta:
        managed = False

    def __init__(self, artist, title):
        self.artist = artist
        self.title = title
        response = requests.get('https://api.lyrics.ovh/v1/' + artist + '/' + title, timeout=10)  # TODO configurable timeout
        logger.debug("Song.Response: " + str(response))
        self.lyrics = response.json()['lyrics']