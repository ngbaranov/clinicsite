from django import template
from cooldoctor.models import TopMenu

register = template.Library()

@register.inclusion_tag('cooldoctor/topmenu.html')
def show_topmenu(menu_class= 'collapse navbar-collapse'):
    article = TopMenu.objects.all()
    return {'article': article, 'menu_class': menu_class }