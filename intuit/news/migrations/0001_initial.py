# Generated by Django 4.0.3 on 2022-04-22 15:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/%Y/%M/%D', verbose_name='Файл')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('image', models.FileField(blank=True, null=True, upload_to='images/%Y/%M/%D', verbose_name='Изображение')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('slug', models.SlugField(unique_for_date='date', verbose_name='Ссылка')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата')),
                ('description', models.TextField(verbose_name='Текст')),
                ('categories', models.ManyToManyField(related_name='categories', to='news.categorymodel', verbose_name='Категории')),
                ('files', models.ManyToManyField(related_name='files', to='news.filemodel', verbose_name='Файлы')),
                ('images', models.ManyToManyField(related_name='images', to='news.imagemodel', verbose_name='Фотографии')),
            ],
            options={
                'ordering': ('date',),
            },
        ),
    ]
