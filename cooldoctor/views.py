from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView




def information(request, pk):

    return render(request,'cooldoctor/information.html')

def index (request):
    return render(request, 'cooldoctor/index.html')

def specialization (request, specialization_id):
    doctors = Doctor.objects.filter(specialization_id=specialization_id)
    specialization = Specialization.objects.get(pk = specialization_id)
    return render(request, 'cooldoctor/specialization.html', {'doctors': doctors, 'specialization': specialization})

# class HeaderInfo(ListView):
#     model = Header
#     template_name = 'cooldoctor/index.html'
#     context_object_name = 'home'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = Header.objects.get(pk = 1).title
#         context['work_hours'] = Header.objects.get(pk = 1).work_hours
#         context['address'] = Header.objects.get(pk = 1).address
#
#         context['slogan'] = Header.objects.get(pk = 1).slogan
#         context['fon'] = Header.objects.get(pk = 1).fon
#
#         return context





# def index(request):
#     return render(request, 'cooldoctor/index.html')


