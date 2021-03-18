from django.test import TestCase

# Create your tests here.
from stats.models import DiscographyStats


class DiscographyStatsTest(TestCase):

    def setUp(self):
        tracks = [
            "these lyrics",
            "are the best lyrics ever",
            "in the world seriously",
            "woop woop"]
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
