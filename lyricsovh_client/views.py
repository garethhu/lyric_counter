import logging

from django.shortcuts import render
from django.http import Http404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import SongSerializer
from .models import Song

logger = logging.getLogger(__name__)

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Song': '/song/<str:artist>/<str:title>'
    }
    return Response(api_urls)

@api_view(['GET'])
def get_song(request, artist, title):
    try:
        song = Song(artist, title)
        serializer = SongSerializer(song, many=False)
        return Response(serializer.data)
    except Exception as e:  # TODO custom exception
        logger.error(e)
        raise Http404

