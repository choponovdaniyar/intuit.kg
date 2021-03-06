# Generated by Django 4.0.3 on 2022-04-22 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorymodel',
            options={'ordering': ('title',), 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='filemodel',
            options={'ordering': ('title',), 'verbose_name': 'Файл', 'verbose_name_plural': 'Файлы'},
        ),
        migrations.AlterModelOptions(
            name='imagemodel',
            options={'ordering': ('title',), 'verbose_name': 'Фото', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AlterModelOptions(
            name='postmodel',
            options={'ordering': ('date',), 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]
