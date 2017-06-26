from django.conf.urls import url
from .views import (
    VideoListView,
    VideoDetailView,
    VideoCreateView,
    VideoUpdateView,
    VideoDeleteView,
    )

app_name = 'videos'
urlpatterns = [
        url(r'^$', VideoListView.as_view(), name='video_list'),
        url(r'^create/$', VideoCreateView.as_view(), name='video_create'),
        url(r'^(?P<slug>[\w-]+)/$', VideoDetailView.as_view(), name='video_detail'),
        url(r'^(?P<slug>[\w-]+)/update/$', VideoUpdateView.as_view(), name='video_update'),
        url(r'^(?P<slug>[\w-]+)/delete/$', VideoDeleteView.as_view(), name='video_delete'),
]
