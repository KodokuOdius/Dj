from django.db import models
from django.urls import reverse, reverse_lazy



class News(models.Model):
    # Наименование поля = Тип (атрибуты)
    # blank - Необязтельное поле

    title = models.CharField(max_length=150, verbose_name="Заголовок")
    content = models.TextField(blank=True, default="Эта новость ещё не созрела =)", verbose_name="Контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата Пуликации")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото", blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    category = models.ForeignKey("Category", on_delete=models.PROTECT, verbose_name="Категория")

    
    # Отображение экземпляра
    def __str__(self) -> str:
        return self.title

    def ma(self):
        return "Hello from model"

    def get_absolute_url(self):
        return reverse("news:view_news", kwargs={"pk": self.pk})

    # Мета-данные
    # Отображение
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

        # Сортировка для отображения 
        ordering = ["-created_at", "title"]



class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Категория")


    def get_absolute_url(self):
        return reverse_lazy("news:category", kwargs={"category_id": self.pk})
    

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

        # Сортировка для отображения 
        ordering = ["title"]
