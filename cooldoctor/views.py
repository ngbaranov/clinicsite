from django.shortcuts import render
from .models import Header
from django.views.generic import ListView, DetailView

class HeaderInfo(ListView):
    model = Header
    template_name = 'cooldoctor/index.html'
    context_object_name = 'home'


def index(request):
    return render(request, 'cooldoctor/index.html')


