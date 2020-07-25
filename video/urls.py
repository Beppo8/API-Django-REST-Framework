from django.urls import path
from .views import ListVideo, DetailVideo

urlpatterns = [
    path('videos/', ListVideo.as_view(), name='lista-video'),
    path('videos/(^?P<pk>[0-9]+)', DetailVideo.as_view(), name='detail-video'),
]