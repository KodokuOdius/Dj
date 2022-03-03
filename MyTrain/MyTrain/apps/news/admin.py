from django.contrib import admin

from .models import News, Category

# Класс в админки
class NewsAdmin(admin.ModelAdmin):
    # Атрибуты для отображения админки
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')

    # Атрибуты с сылками для редактирования
    list_display_links = ('id', 'title')

    # Атрибут для поиска
    search_fields = ('title', 'content')

    # Редактируемые поля из списка 
    list_editable = ('is_published',)

    # Фильтр
    list_filter = ('is_published', 'category')



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


# Регистрация Класса в админки
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

