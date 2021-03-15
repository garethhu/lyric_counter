import logging

from django.http import Http404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from stats.models import DiscographyStats

logger = logging.getLogger(__name__)

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'AvgLen': '/stats/avglen/<str:artist>',
        'MinLen': '/stats/minlen/<str:artist>',
        'MaxLen': '/stats/maxlen/<str:artist>',
        'VarLen': '/stats/varlen/<str:artist>',
        'SdLen': '/stats/sdlen/<str:artist>',
    }
    return Response(api_urls)

@api_view(['GET'])
def get_avg_len(request, artist):
    try:
        disc_stats = DiscographyStats.disc_stats(artist)
        return Response(disc_stats.avg_track_length)
    except Exception as e: #  TODO custom exception
        logger.error(e)
        raise Http404

@api_view(['GET'])
def get_min_len(request, artist):
    try:
        disc_stats = DiscographyStats.disc_stats(artist)
        return Response(disc_stats.min_track_length)
    except Exception as e: #  TODO custom exception
        logger.error(e)
        raise Http404

@api_view(['GET'])
def get_max_len(request, artist):
    try:
        disc_stats = DiscographyStats.disc_stats(artist)
        return Response(disc_stats.max_track_length)
    except Exception as e: #  TODO custom exception
        logger.error(e)
        raise Http404

@api_view(['GET'])
def get_var_len(request, artist):
    try:
        disc_stats = DiscographyStats.disc_stats(artist)
        return Response(disc_stats.var_track_length)
    except Exception as e: #  TODO custom exception
        logger.error(e)
        raise Http404

@api_view(['GET'])
def get_sd_len(request, artist):
    try:
        disc_stats = DiscographyStats.disc_stats(artist)
        return Response(disc_stats.sd_track_length)
    except Exception as e: #  TODO custom exception
        logger.error(e)
        raise Http404