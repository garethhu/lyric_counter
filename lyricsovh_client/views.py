from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def get_song(request, artist, title):
    response_obj = {
        "artist": artist,
        "title": title
    }
    try:
        song = []
        response_obj['lyrics'] = song.lyrics
    except Exception as e:
        response_obj['error_msg'] = 'An error occurred getting song from artist'
        response_obj['exception'] = e

    return Response(response_obj)