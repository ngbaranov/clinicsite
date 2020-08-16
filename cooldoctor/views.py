from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView

class ViewArticle(DetailView):
    model = Article

class ViewDoctor(DetailView):
    model = Doctor
    # template_name = 'cooldoctor/view_doctor.html'



class Discount (DetailView):
    model = Discounts
    template_name = 'cooldoctor/discounts.html'
    context_object_name = 'discount'

    def get_queryset(self):
        return Discounts.objects.filter(pk = self.kwargs['pk'])


class Information(DetailView):
    model = TopMenu
    template_name = 'cooldoctor/information.html'
    context_object_name = 'inf_view'


class SpecDoctor(ListView):
    model = Doctor
    template_name = 'cooldoctor/specialization.html'
    context_object_name = 'doctors'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Specialization.objects.get(pk=self.kwargs['specialization_id'])
        return context

    def get_queryset(self):
        return  Doctor.objects.filter(specialization_id=self.kwargs['specialization_id'])


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


