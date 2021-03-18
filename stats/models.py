from concurrent.futures import ThreadPoolExecutor, wait

from django.db import models

import logging
import string
import statistics
import numpy

# Create your models here.
from lyricsovh_client.models import Song
from musicbrainzngs_client.models import Artist

logger = logging.getLogger(__name__)

_disc_stats = {}


class DiscographyStats(models.Model):
    _avg_track_length = models.FloatField()
    _min_track_length = models.IntegerField()
    _max_track_length = models.IntegerField()
    _var_track_length = models.FloatField()
    _sd_track_length = models.FloatField()

    class Meta:
        managed = False

    @staticmethod
    def get_song(artist_name, name):
        try:
            return Song.new_song(artist_name, name)
        except Exception as e:
            logger.error(e)
            return None

    @classmethod
    def disc_stats(cls, artist_name):
        if artist_name not in _disc_stats:
            artist = Artist(artist_name)
            track_names = artist.tracks
            pool = ThreadPoolExecutor(32)  # TODO make this configurable
            song = lambda name: DiscographyStats.get_song(artist_name, name)
            tracks_fut = [pool.submit(song, name) for name in track_names]
            tracks = filter(lambda track: track is not None, [track_fut.result() for track_fut in tracks_fut])
            _disc_stats[artist_name] = cls(tracks)
        return _disc_stats[artist_name]

    def __init__(self, tracks):
        super().__init__()
        self._track_lengths = None
        self.tracks = tracks

    @property
    def avg_track_length(self):
        return statistics.mean(self.track_lengths)

    @property
    def min_track_length(self):
        return min(self.track_lengths)

    @property
    def max_track_length(self):
        return max(self.track_lengths)

    @property
    def var_track_length(self):
        return numpy.var(self.track_lengths)

    @property
    def sd_track_length(self):
        return numpy.std(self.track_lengths)

    @property
    def track_lengths(self):
        if self._track_lengths is None:
            logger.debug("DiscographyStats: Calculating track tokens")
            tracks_tokens = [track.lyrics.strip(string.punctuation).split() for track in self.tracks]
            logger.debug("DiscographyStats.Tokens: " + str(tracks_tokens))
            logger.debug("DiscographyStats: Calculating track lengths")
            self._track_lengths = [sum([track_token.isalpha() for track_token in track_tokens]) for track_tokens in
                                   tracks_tokens]
            logger.debug("DiscographyStats.TrackLengths: " + str(self._track_lengths))
        return self._track_lengths
