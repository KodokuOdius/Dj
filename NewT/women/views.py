from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import Women


menu = [
    {'title': 'About site', 'url_name': 'women:about'},
    {'title': 'Add page', 'url_name': 'women:add_page'},
    {'title': 'Contact us', 'url_name': 'women:contact'},
    {'title': 'Log In', 'url_name': 'women:login'}
]

def index(request): #HttpRequest
    posts = Women.objects.all()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Main page'
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', context={'menu': menu, 'title': 'About site'})


def add_page(request):
    return HttpResponse('<h1>Add page</h1>')


def contact(request):
    return HttpResponse('<h1>Contact us</h1>')


def login(request):
    return HttpResponse('<h1>Log In</h1>')


def show_post(request, post_id):
    return HttpResponse(f'<h1>We are showing your this post id = {post_id}</h1>')


def categories(request, cat):
    return HttpResponse(f"<h1>Категория! <p>{cat}</p></h1>")


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