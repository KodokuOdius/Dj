from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Article, Comment

def index(request):
    lasts = Article.objects.order_by('-public_date')[:5]
    return render(request, 'articles/list.html', {'lasts': lasts})

def detail(request, article_id):
    try:
        art = Article.objects.get(id=article_id)
    except Exception:
        raise Http404("Статья не найдена")

    last = art.comment_set.order_by('-id')[:10]

    return render(request, 'articles/detail.html', {'article': art, 'last': last})

def leave_comment(request, article_id):
    try:
        art = Article.objects.get(id=article_id)
    except Exception:
        raise Http404("Статья не найдена")

    art.comment_set.create(autor_name=request.POST['name'], comment_text=request.POST['text'])

    return HttpResponseRedirect( reverse("articles:detail", args=(art.id,)) )

def test(request):
    return HttpResponse('Test page')