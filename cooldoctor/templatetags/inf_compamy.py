from django import template
from cooldoctor.models import Header

register = template.Library()

@register.inclusion_tag('cooldoctor/inf_company.html')
def inf_company(menu_class = 'main-promo'):
    inf = Header.objects.get(pk = 1)
    return {'inf': inf, 'menu_class': menu_class}