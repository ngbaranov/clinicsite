from django import template
from cooldoctor.models import Specialization

register = template.Library()

@register.inclusion_tag('cooldoctor/view_specialization.html')
def view_specialization():
    view_spec = Specialization.objects.all()
    return {'view_spec': view_spec}