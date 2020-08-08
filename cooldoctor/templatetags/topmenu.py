from django import template
from cooldoctor.models import TopMenu, Avatar

register = template.Library()

@register.inclusion_tag('cooldoctor/topmenu.html')
def show_topmenu(menu_class= 'navbar navbar-expand-sm'):
    article = TopMenu.objects.all()

    logo = Avatar.objects.get(pk = 1).avatar
    return {'article': article, 'menu_class': menu_class, 'logo': logo }

