from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
import random

def home(request):
    return render(request, 'home.html', {})


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'name': 'Iakovos',
            'random_number': random.randint(1,500)
        }
        return render(request, 'home.html', context)
