from django.urls import path

from . import views

# Ссылки по которым можно перейти на станицу
app_name = 'micro_server'
urlpatterns = [
    path('', views.msg, name="msg"), # Главная
]
