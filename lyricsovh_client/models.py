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

    @classmethod
    def new_song(cls, artist, title):
        response = requests.get('https://api.lyrics.ovh/v1/' + artist + '/' + title,
                                timeout=10)  # TODO configurable timeout
        logger.debug("Song.Response: " + str(response))
        lyrics = response.json()['lyrics']
        return cls(artist, title, lyrics)

    def __init__(self, artist, title, lyrics):
        self.artist = artist
        self.title = title
        self.lyrics = lyrics