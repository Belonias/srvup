import random
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
        CreateView,
        DetailView,
        ListView,
        UpdateView,
        DeleteView
    )

from .forms import VideoForm
from .mixins import MemberRequiredMixin, StaffMemberRequiredMixin
from .models import Video


class VideoCreateView(StaffMemberRequiredMixin, CreateView):
    model = Video
    form_class = VideoForm
    #success_url = "/success/"


class VideoDetailView(MemberRequiredMixin, DetailView):
    queryset = Video.objects.all()


class VideoListView(ListView):

    def get_queryset(self):
        request = self.request
        queryset = Video.objects.all()
        query = request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(VideoListView, self).get_context_data(*args, **kwargs)
        context['random_number'] = random.randint(100, 10000)
        print(context)
        return context


class VideoUpdateView(UpdateView):
    queryset = Video.objects.all()
    form_class = VideoForm


class VideoDeleteView(DeleteView):
    queryset = Video.objects.all()
    success_url = '/videos/'
