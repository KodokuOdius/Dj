from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse


from .models import News, Category

# Функция для отображения странички
def index(request):
    news = News.objects.order_by("-created_at")
    categories = Category.objects.all()

    context = {
        "news": news, 
        "title": "Список новоствей",
        "categories": categories
    }

    return render(
        request, 
        "news/index.html", 
        context=context
    )


def test(request):
    return HttpResponse("Hello, World!")



def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)

    context = {
        "news": news,
        "categories": categories,
        "category": category
    }

    return render(
        request,
        template_name="news/category.html",
        context=context
    )
