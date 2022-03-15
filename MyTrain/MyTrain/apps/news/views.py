from re import template
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponse
from django.views.generic import ListView, DetailView, CreateView


from .models import News, Category
from .forms import NewsForm



class NomeNews(ListView): # То же что и index()
    model = News

    template_name = "news/index.html"
    context_object_name = "news"

    # Для статичных объектов
    # extra_context = {
    #     "title": "Главная"
    # }

    # Для динамики
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная страница"

        return context

    # Получение нужных данный - фильтрация
    def get_queryset(self):
        return News.objects.filter(is_published=True)

"""
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
"""


class NewsByCategory(ListView):
    model = News

    template_name = "news/index.html"
    context_object_name = "news"
    allow_empty = False

    # SELECT * FROM News WHERE category_id = Номер из kwargs AND is_published = True
    def get_queryset(self):
        return News.objects.filter(
            category_id=self.kwargs["category_id"],
            is_published=True
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = Category.objects.get(pk=self.kwargs["category_id"])
        #print(News.objects.get())
        print(context)

        return context

"""
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
"""


class ViewNews(DetailView):
    model = News
    #pk_url_kwarg = "news_id"

    template_name = "news/view_news.html"
    context_object_name = "news_item"
    
"""
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
"""



def test(request):
    return HttpResponse("Hello, World!")

def secret(request):
    import requests as req
    return HttpResponse(req.get("https://pornhub.com/").content)




class CreateNews(CreateView):
    form_class = NewsForm

    template_name = "news/add_news.html"
    pass



def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)

            #news = News.objects.create(**form.cleaned_data)


            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()


    return render(
        request=request,
        template_name="news/add_news.html",
        context={"form": form}
    )

