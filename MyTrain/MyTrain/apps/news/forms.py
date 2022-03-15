from django import forms
from .models import News
from django.core.exceptions import ValidationError
import re


class NewsForm(forms.ModelForm):
    # label - Название поля, отображение на странице
    # reqired - Важность поля (обязательно/необязательно)
    # queryset - множество для списов
    # initial - по умолчанию
    # empty_label - пустой список (начальный)
    # widget - атрибуты для html кода и уточнение принадлежности к тегу

    # Не связанныя с моделью форма
    # title = forms.CharField(
    #     max_length=150, 
    #     label="Заголовок", 
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control"
    #         }
    #     )
    # )
    # content = forms.CharField(
    #     label="Содержание", 
    #     required=False, 
    #     widget=forms.Textarea(
    #         attrs={
    #             "class": "form-control",
    #             "rows": 4
    #         }
    #     )
    # )

    # category = forms.ModelChoiceField(
    #     queryset=Category.objects.all(),
    #     empty_label="Выберите категорию",
    #     label="Категория", 
    #     widget=forms.Select(
    #         attrs={
    #             "class": "form-control"
    #         }
    #     )
    # )

    # is_published = forms.BooleanField(
    #     label="Опубликовать", 
    #     initial=True
    # )



    class Meta:
        model = News
        # fields = '__all__'

        fields = ['title', 'content', 'category', 'is_published']

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4
                }
            ),
            "category": forms.Select(
                attrs={
                    "class": "form-control"
                }
            )
        }


    # Персональная валидация
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r"\b\d", title):
            raise ValidationError("Название не должно начинаться с цифры")

        return title.upper()



