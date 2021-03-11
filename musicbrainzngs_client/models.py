from django.db import models
from jsonfield import JSONField

import musicbrainzngs

# Create your models here.
musicbrainzngs.set_useragent("lyrics_counter", "v0.1", "garethjhumphries@gmail.com")

class Artist(models.Model):
    artist = models.CharField(max_length=100)
    artist_id = models.CharField(max_length=36)
    tracks = JSONField()

    class Meta:
        managed = False

    def __init__(self, artist):
        self.artist = artist
        self.artist_id = musicbrainzngs.search_artists(artist=artist)['artist-list'][0]['id'] #  TODO apply checking in case match is partial
        works = musicbrainzngs.get_artist_by_id(self.artist_id, includes=["works"])
        self.tracks = [work['title'] for work in works['artist']['work-list']]

