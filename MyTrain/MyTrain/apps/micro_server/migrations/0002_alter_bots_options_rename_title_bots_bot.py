# Generated by Django 4.0.2 on 2022-03-16 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('micro_server', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bots',
            options={'ordering': ['bot'], 'verbose_name': 'Бот', 'verbose_name_plural': 'Боты'},
        ),
        migrations.RenameField(
            model_name='bots',
            old_name='title',
            new_name='bot',
        ),
    ]
