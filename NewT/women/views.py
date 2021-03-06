from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AddPostForm
from .models import Category, Women
from .utils import *


class WomenHome(DataMixin, ListView):
    model = Women
    template_name = "women/index.html"
    context_object_name = "posts"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Main page")
                
        return context | c_def


    def get_queryset(self):
        return Women.objects.filter(is_published=True)

# def index(request): #HttpRequest
#     posts = Women.objects.all()

#     context = {
#         'posts': posts,
#         'title': 'Main page',
#         'category_selected': 0

#     }
#     return render(request, 'women/index.html', context=context)



class WomenCategory(DataMixin, ListView):
    model = Women
    template_name = "women/index.html"
    context_object_name = "posts"
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title="Category::" + str(context["posts"][0].category),
            category_selected=context["posts"][0].category_id
        )

        return context | c_def

    def get_queryset(self):
        return Women.objects.filter(
            category__slug=self.kwargs["category_slug"],
            is_published=True
        )

# def category(request, category_slug):
#     category = get_object_or_404(Category, slug=category_slug)
#     posts = Women.objects.filter(category_id=category.id)
#     if not posts:
#         raise Http404

#     context = {
#         'posts': posts,
#         'title': 'Categories',
#         'category_selected': category.id

#     }
#     return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html', context={'title': 'About site'})



class AddPost(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = "women/add_page.html"
    success_url = reverse_lazy("women:home")
    login_url = reverse_lazy("women:home")
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="???????????????????? ????????????")

        return context | c_def
    

# def add_page(request):
#     if request.method == "POST":
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             try:
#                 form.save()
#                 return redirect("women:home")
#             except Exception as ex: 
#                 form.add_error(None, "Error")
#     else:
#         form = AddPostForm()
#     context = {
#         'title': '???????????????????? ????????????',
#         'form': form
#     }
#     return render(request, 'women/add_page.html', context=context)


def contact(request):
    return HttpResponse('<h1>Contact us</h1>')


def login(request):
    return HttpResponse('<h1>Log In</h1>')



class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = "women/post.html"
    slug_url_kwarg = "post_slug"
    # pk_url_kwarg = "post_id"

    context_object_name = "post"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context["post"].title)

        return context | c_def
    

# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)

#     context = {
#         'post': post,
#         'title': post.title,
#         'category_selected': post.category_id
#     }

#     return render(request, 'women/post.html', context=context)





def arc(request, year):
    # redirect - 302 = redirect
    # redirect - 301 = redirect + permanent=True
    if int(year) > 2022:
        return redirect('home', permanent=True)
        # raise Http404()

    return HttpResponse(f"?????????? - {year} ??????")


def pageNotFound(request, exception):
    page_404 = """
    <div>
        <img class="marginauto" src="https://www.animesxis.com.br/wp-content/uploads/2016/12/erro-404-anime-xis.jpg" alt="???????????????????????????????? ??????????????????????" />
    </div>

    <style>
        .marginauto {
            margin: 10px auto 20px;
            display: block;
        }
    </style>
    """

    return HttpResponseNotFound(page_404)
