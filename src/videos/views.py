from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
    )
from .models import Video
from .forms import VideoForm

import random

# Create your views here.
class VideoCreateView(CreateView):
    model = Video
    form_class = VideoForm


class VideoDetailView(DetailView):
    queryset = Video.objects.all()

    def get_object(self):
        return get_object_or_404(Video, slug=self.kwargs.get('abc'))

    def get_context_data(self, *args, **kwargs):
        context = super(VideoDetailView, self).get_context_data(*args, **kwargs)
        return context


class VideoListView(ListView):
    queryset = Video.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(VideoListView, self).get_context_data(*args, **kwargs)
        print(context)
        context['random'] = random.randint(1,500)
        return context


class VideoUpdateView(UpdateView):
    queryset = Video.objects.all()
    pass


class VideoDeleteView(DeleteView):
    queryset = Video.objects.all()
    pass
