# Generated by Django 4.0.2 on 2022-03-24 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_news_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='views',
        ),
    ]