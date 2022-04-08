from argparse import HelpFormatter
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import Category, Women
from .forms import AddPostForm



def index(request): #HttpRequest
    posts = Women.objects.all()

    context = {
        'posts': posts,
        'title': 'Main page',
        'category_selected': 0

    }
    return render(request, 'women/index.html', context=context)


def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = Women.objects.filter(category_id=category.id)
    if not posts:
        raise Http404

    context = {
        'posts': posts,
        'title': 'Categories',
        'category_selected': category.id

    }
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', context={'title': 'About site'})


def add_page(request):
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                form.save()
                return redirect("women:home")
            except Exception as ex: 
                form.add_error(None, "Error")
    else:
        form = AddPostForm()


    context = {
        'title': 'Добавление статьи',
        'form': form
    }
    return render(request, 'women/add_page.html', context=context)


def contact(request):
    return HttpResponse('<h1>Contact us</h1>')


def login(request):
    return HttpResponse('<h1>Log In</h1>')


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'title': post.title,
        'category_selected': post.category_id
    }

    return render(request, 'women/post.html', context=context)





def arc(request, year):
    # redirect - 302 = redirect
    # redirect - 301 = redirect + permanent=True
    if int(year) > 2022:
        return redirect('home', permanent=True)
        # raise Http404()

    return HttpResponse(f"Архив - {year} год")


def pageNotFound(request, exception):
    page_404 = """
    <div>
        <img class="marginauto" src="https://www.animesxis.com.br/wp-content/uploads/2016/12/erro-404-anime-xis.jpg" alt="отцентрированное изображение" />
    </div>

    <style>
        .marginauto {
            margin: 10px auto 20px;
            display: block;
        }
    </style>
    """

    return HttpResponseNotFound(page_404)