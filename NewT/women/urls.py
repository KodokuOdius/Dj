from django.urls import path, re_path
from . import views


app_name = 'women'
urlpatterns = [
    path('', views.index, name='home'),
    path('cat/', views.categories),
    path('cat/<slug:cat>/', views.categories),
    re_path(r'^arc/(?P<year>[0-9]{0,4})/', views.arc),
    path('about/', views.about, name='about'),
    path('addpage/', views.add_page, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<int:post_id>/', views.show_post, name='post')
]
