# Generated by Django 4.0.2 on 2022-03-16 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Бот')),
            ],
            options={
                'verbose_name': 'Бот',
                'verbose_name_plural': 'Боты',
                'ordering': ['title'],
            },
        ),
    ]
