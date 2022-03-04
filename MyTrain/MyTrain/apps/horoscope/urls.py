from django.urls import path

from . import views

# Ссылки по которым можно перейти на станицу
app_name = 'horoscope'
urlpatterns = [
    path('', views.index, name="index"), # Главная
    path('secret/', views.secret, name="secret"),
    path('<sign_of_zodiac>/', views.zodiac_info, name="zodiac_info")
]
