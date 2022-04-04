from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, Http404

def index(request): #HttpRequest
    return HttpResponse("Hello, World!")


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