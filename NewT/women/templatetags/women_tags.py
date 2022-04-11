from django import template
from women.models import *

register = template.Library()

@register.simple_tag(name="get_categories")
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, category_selected=0):
    if not sort:
        categories = get_categories()
    else:
        categories = Category.objects.order_by(sort)

    return {"categories": categories, "category_selected": category_selected}


@register.simple_tag(name="get_menu")
def get_menu():
    menu = [
        {'title': 'About site', 'url_name': 'women:about'},
        {'title': 'Add page', 'url_name': 'women:add_page'},
        {'title': 'Contact us', 'url_name': 'women:contact'},
        {'title': 'Log In', 'url_name': 'women:login'}
    ]

    return menu
