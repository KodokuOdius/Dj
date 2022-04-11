from django.urls import path, re_path
from . import views


app_name = 'women'
urlpatterns = [
    path('', views.WomenHome.as_view(), name='home'),
    # path('cat/<slug:cat>/', views.categories),
    re_path(r'^arc/(?P<year>[0-9]{0,4})/', views.arc),
    path('about/', views.about, name='about'),
    path('addpage/', views.AddPost.as_view(), name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('category/<slug:category_slug>', views.WomenCategory.as_view(), name="category")
]
