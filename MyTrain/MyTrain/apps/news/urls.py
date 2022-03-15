from django.urls import path

from . import views

# Ссылки по которым можно перейти на станицу
app_name = 'news'
urlpatterns = [
    # path('', views.index, name='home'),
    path('', views.NomeNews.as_view(), name='home'),
    path('test', views.test, name='test'),
    path('secret', views.secret, name='secret'),
    # path('category/<int:category_id>', views.category, name='category'),
    path('category/<int:category_id>', views.NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>', views.ViewNews.as_view(), name='view_news'),
    # path('news/add-news', views.add_news, name='add_news')
    path('news/add-news', views.CreateNews.as_view(), name='add_news')
]