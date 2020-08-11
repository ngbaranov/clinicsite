from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView




def information(request, pk):

    return render(request,'cooldoctor/information.html')

# def index (request):
#     return render(request, 'cooldoctor/index.html')

def specialization (request, specialization_id):
    doctors = Doctor.objects.filter(specialization_id=specialization_id)
    specialization = Specialization.objects.get(pk = specialization_id)
    return render(request, 'cooldoctor/specialization.html', {'doctors': doctors, 'specialization': specialization})

class Home(ListView):
    model = Action
    template_name = 'cooldoctor/index.html'
    context_object_name = 'home'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['discounts'] = Discounts.objects.all()
        context['doctor'] = Doctor.objects.all().all()[:3]
        context['article'] =  Article.objects.all()

        return context





# def index(request):
#     return render(request, 'cooldoctor/index.html')


