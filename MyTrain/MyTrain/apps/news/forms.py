from unicodedata import category
from django import forms
from .models import Category


class NewsForm(forms.Form):
    # label - Название поля, отображение на странице
    # reqired - Важность поля (обязательно/необязательно)
    # queryset - множество для списов
    # initial - по умолчанию
    # empty_label - пустой список (начальный)
    # widget - атрибуты для html кода и уточнение принадлежности к тегу

    title = forms.CharField(
        max_length=150, 
        label="Заголовок", 
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    content = forms.CharField(
        label="Содержание", 
        required=False, 
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 4
            }
        )
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Выберите категорию",
        label="Категория", 
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )

    is_published = forms.BooleanField(
        label="Опубликовать", 
        initial=True
    )

    class Meta:
        pass


