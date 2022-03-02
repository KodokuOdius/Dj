from django.urls import path

from . import views

# Ссылки по которым можно перейти на станицу
app_name = 'news'
urlpatterns = [
    path('', views.index, name="index"),
    path('test', views.test, name="test")
]