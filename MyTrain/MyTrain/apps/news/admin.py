
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category

# Класс в админки
class NewsAdmin(admin.ModelAdmin):
    # Атрибуты для отображения админки
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo')

    # Атрибуты с сылками для редактирования
    list_display_links = ('id', 'title')

    # Атрибут для поиска
    search_fields = ('title', 'content')

    # Редактируемые поля из списка 
    list_editable = ('is_published',)

    # Фильтр
    list_filter = ('is_published', 'category')

    fields = ('title', 'category', 'content', 'photo', 'get_photo', 'is_published',
    'views', 'created_at', 'updated_at')

    readonly_fields = ('get_photo', 'views', 'created_at', 'updated_at')
    

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return "-"

    get_photo.short_desctiption = "Миниатюра"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


# Регистрация Класса в админки
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

