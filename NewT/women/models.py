from tabnanny import verbose
from django.db import models
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name='Содержание')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фотография')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    # models.CASCADE - delete notes
    # models.PROTECT - cansel
    # models.SET_NULL - set null
    # models.SER_DEFAULT - set default value
    # models.SET() - set users's (personal) value
    # models.DO_NOTHING - nothing

    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self) -> str:
        return self.title

    
    def get_absolute_url(self):
        return reverse("women:post", kwargs={"post_slug": self.slug})


    class Meta:
        verbose_name = "Известные женщины"
        verbose_name_plural = "Известные женщины"
        ordering = ['-time_create', 'title']

  
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("women:category", kwargs={"category_slug": self.slug})

    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    