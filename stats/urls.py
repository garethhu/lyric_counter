from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('avglen/<str:artist>', views.get_avg_len, name='avg-len-get'),
    path('minlen/<str:artist>', views.get_min_len, name='min-len-get'),
    path('maxlen/<str:artist>', views.get_max_len, name='max-len-get'),
    path('varlen/<str:artist>', views.get_var_len, name='var-len-get'),
    path('sdlen/<str:artist>', views.get_sd_len, name='sd-len-get'),
]