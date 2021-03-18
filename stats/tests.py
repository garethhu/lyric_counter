from django.test import TestCase

# Create your tests here.
from lyricsovh_client.models import Song
from stats.models import DiscographyStats


# TODO use a test template with more examples and covering unhappy paths and edge cases
class DiscographyStatsTest(TestCase):

    def setUp(self):
        tracks = [
            Song("artist1", "song1", "these lyrics"),
            Song("artist1", "song2", "are the best lyrics ever"),
            Song("artist1", "song3", "in the world seriously"),
            Song("artist1", "song4", "woop woop")
        ]
        self.stats = DiscographyStats(tracks)

    def test_avg_len(self):
        self.assertEqual(self.stats.avg_track_length, 3.25)

    def test_min_len(self):
        self.assertEqual(self.stats.min_track_length, 2)

    def test_max_len(self):
        self.assertEqual(self.stats.max_track_length, 5)

    def test_var_len(self):
        self.assertEqual(self.stats.var_track_length, 1.6875)

    def test_sd_len(self):
        self.assertEqual(self.stats.sd_track_length, 1.299038105676658)
