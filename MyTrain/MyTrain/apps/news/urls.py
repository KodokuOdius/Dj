from django.urls import path

from . import views

# Ссылки по которым можно перейти на станицу
app_name = 'news'
urlpatterns = [
    path('', views.index, name='home'),
    path('test', views.test, name='test'),
    path('category/<int:category_id>', views.get_category, name='category')
]