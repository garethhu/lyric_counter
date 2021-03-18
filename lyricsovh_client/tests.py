from unittest.mock import patch

from django.test import TestCase

import requests

# Create your tests here.
from lyricsovh_client.models import Song


# TODO use a test template with more examples and covering unhappy paths and edge cases
class SongTest(TestCase):

    def setUp(self):
        self.artist = "artist01"
        self.title = "title01"
        self.lyrics = "these lyrics are the best"

    @patch('lyricsovh_client.models.requests.get')
    def test_new_song(self, mock_get):
        endpoint_resp = requests.Response()
        endpoint_resp._content = b"""
        {
            "lyrics": "these lyrics are the best"
        }
        """

        mock_get.return_value = endpoint_resp

        response = Song.new_song(self.artist, self.title)

        self.assertEqual(response.artist, self.artist)
        self.assertEqual(response.title, self.title)
        self.assertEqual(response.lyrics, self.lyrics)
