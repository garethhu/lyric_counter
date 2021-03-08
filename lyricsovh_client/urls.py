from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('song/<str:artist>/<str:title>', views.get_song, name='song-get')
]