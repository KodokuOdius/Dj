from django.urls import path, re_path
from . import views


app_name = 'women'
urlpatterns = [
    path('', views.index, name='home'),
    path('cat/', views.categories),
    path('cat/<slug:cat>/', views.categories),
    re_path(r'^arc/(?P<year>[0-9]{4})/', views.arc)
]
