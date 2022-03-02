from django.shortcuts import render
from django.http import HttpResponse


from .models import News

# Функция для отображения странички
def index(request):
    news = News.objects.order_by("-created_at")
    return render(request, 'news/index.html', {'news': news, "title": "Список новоствей"})



def test(request):
    return HttpResponse("Hello, World!")

