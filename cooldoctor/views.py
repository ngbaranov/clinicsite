from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView




class ViewTopmenu(DetailView):
    model = TopMenu
    context_object_name = 'top_menu'



class HeaderInfo(ListView):
    model = Header
    template_name = 'cooldoctor/index.html'
    context_object_name = 'home'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Header.objects.get(pk = 1).title
        context['work_hours'] = Header.objects.get(pk = 1).work_hours
        context['address'] = Header.objects.get(pk = 1).address
        context['avatar'] = Header.objects.get(pk = 1).avatar
        context['slogan'] = Header.objects.get(pk = 1).slogan
        context['fon'] = Header.objects.get(pk = 1).fon

        return context





# def index(request):
#     return render(request, 'cooldoctor/index.html')


