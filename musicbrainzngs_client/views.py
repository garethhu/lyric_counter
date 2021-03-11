import logging

from django.http import Http404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ArtistSerializer
from .models import Artist

logger = logging.getLogger(__name__)

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Artist': '/artist/<str:artist>'
    }
    return Response(api_urls)

@api_view(['GET'])
def get_artist(request, artist_name):
    try:
        artist = Artist(artist_name)
        serializer = ArtistSerializer(artist, many=False)
        return Response(serializer.data)
    except Exception as e: #  TODO custom exception
        logger.error(e)
        raise Http404