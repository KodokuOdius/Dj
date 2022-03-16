from tabnanny import verbose
from turtle import title
from django.db import models

# Create your models here.

class Bots(models.Model):
    bot = models.CharField(max_length=150, db_index=True, verbose_name="Бот")

    def __str__(self) -> str:
        return self.bot

    class Meta:
        verbose_name = "Бот"
        verbose_name_plural = "Боты"

        # Сортировка для отображения 
        ordering = ["bot"]



class MSG(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name="Заголовок"
    )
    content = models.TextField(default="Эта новость ещё не созрела =)", verbose_name="Содержание")
    publication = models.DateTimeField(auto_now_add=True, verbose_name="Дата Пуликации")
    select = models.ForeignKey("Bots", on_delete=models.PROTECT, default=3 , verbose_name="Боты")


    def __str__(self) -> str:
        return self.title, self.publication


    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

        ordering = ["-publication", "title"]

    