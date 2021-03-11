from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('artist/<str:artist_name>', views.get_artist, name='artist-get')
]