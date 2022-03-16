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