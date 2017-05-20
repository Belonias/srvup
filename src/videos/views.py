from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
    )
from .models import Video

# Create your views here.
class VideoCreateView(CreateView):
    queryset = Video.objects.all()
    pass


class VideoDetailView(DetailView):
    queryset = Video.objects.all()
    pass


class VideoListView(ListView):
    queryset = Video.objects.all()
    pass


class VideoUpdateView(UpdateView):
    queryset = Video.objects.all()
    pass


class VideoDeleteView(DeleteView):
    queryset = Video.objects.all()
    pass
