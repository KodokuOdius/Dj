from django.db import models



class News(models.Model):
    # Наименование поля = Тип (атрибуты)
    # blank - Необязтельное поле

    title = models.CharField(max_length=150, verbose_name="Заголовок")
    content = models.TextField(blank=True, default="Эта новость ещё не созрела =)", verbose_name="Контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата Пуликации")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото", blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True, verbose_name="Категория")

    # Отображение экземпляра
    def __str__(self) -> str:
        return self.title

    def ma(self):
        return "Hello from model"

    # Мета-данные
    # Отображение
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

        # Сортировка для отображения 
        ordering = ["-created_at", "title"]



class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Категория")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

        # Сортировка для отображения 
        ordering = ["title"]
    pass
