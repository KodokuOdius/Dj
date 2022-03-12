from django import template

from news.models import Category

# Создание и регистрация пресональных тегов

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag("news/inc/list_categories.html")
def show_categories(a="Hello", b="World"):
    categories = get_categories()
    return {"categories" : categories, "a": a, "b": b}