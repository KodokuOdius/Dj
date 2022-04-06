from django.db import models
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    # models.CASCADE - delete notes
    # models.PROTECT - cansel
    # models.SET_NULL - set null
    # models.SER_DEFAULT - set default value
    # models.SET() - set users's (personal) value
    # models.DO_NOTHING - nothing

    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self) -> str:
        return self.title

    
    def get_absolute_url(self):
        return reverse("women:post", kwargs={"post_id": self.pk})

  
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("women:category", kwargs={"category_id": self.pk})
    