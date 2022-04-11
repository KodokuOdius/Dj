from django.db.models import Count

from .models import *


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        category = Category.objects.annotate(Count('women'))
        context["categories"] = category

        if "category_selected" not in context:
            context["category_selected"] = 0

        return context
