from django import forms
from django.core.exceptions import ValidationError
import re

from .models import Bots


class MSG(forms.Form):
    # label - Название поля, отображение на странице
    # reqired - Важность поля (обязательно/необязательно)
    # queryset - множество для списов
    # initial - по умолчанию
    # empty_label - пустой список (начальный)
    # widget - атрибуты для html кода и уточнение принадлежности к тегу

    # Не связанныя с моделью форма

    title = forms.CharField(
        max_length=150, 
        label="Заголовок Сообщения", 
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    content = forms.CharField(
        label="Сообщение", 
        required=False, 
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 4
            }
        )
    )
    # Category.objects.all()

    l = None

    select = forms.ModelChoiceField(
        queryset=Bots.objects.all(),
        empty_label="Выберите ботов",
        label="Категория", 
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )



    # Персональная валидация
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r"\b\d", title):
            raise ValidationError("Название не должно начинаться с цифры")

        return title.upper()



