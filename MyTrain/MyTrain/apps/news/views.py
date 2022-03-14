from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponse


from .models import News, Category
from .forms import NewsForm

# Функция для отображения странички
def index(request):
    news = News.objects.order_by("-created_at")

    context = {
        "news": news, 
        "title": "Список новоствей"
    }

    return render(
        request, 
        "news/index.html", 
        context=context
    )


def test(request):
    return HttpResponse("Hello, World!")



def category(request, category_id):
    news = News.objects.filter(category_id=category_id)

    context = {
        "news": news
    }

    return render(
        request,
        template_name="news/category.html",
        context=context
    )


def view_news(request, news_id):
    news_item = get_object_or_404(
        News,
        pk=news_id
    )

    return render(
        request=request,
        template_name="news/view_news.html",
        context= {
            "news_item": news_item
        }
    )

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            news = News.objects.create(**form.cleaned_data)
            return redirect(news)
    else:
        form = NewsForm()


    return render(
        request=request,
        template_name="news/add_news.html",
        context={"form": form}
    )

