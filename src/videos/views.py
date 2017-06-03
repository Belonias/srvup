from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
    )
from .models import Video
import random

# Create your views here.
class VideoCreateView(CreateView):
    queryset = Video.objects.all()
    pass


class VideoDetailView(DetailView):
    queryset = Video.objects.all()
    pass


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
