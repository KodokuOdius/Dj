from django.urls import path

from . import views

# Ссылки по которым можно перейти на станицу
app_name = 'horoscope'
urlpatterns = [
    path('', views.index, name="index")
]