from django import forms
from .models import *
import re


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Категория не выбрана"


    def clean_title(self):
        title = self.cleaned_data['title']
        if re.findall(r"\b[0-9]+", title):
            raise forms.ValidationError("ЧИСЛООООООООООООО!")


        if len(title) > 150:
            raise forms.ValidationError("Длина больше 150 символов")
        
        return title


    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'category']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 4})
        }