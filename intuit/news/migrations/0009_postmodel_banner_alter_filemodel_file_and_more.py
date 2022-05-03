# Generated by Django 4.0.3 on 2022-04-24 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_alter_postmodel_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='banner',
            field=models.FileField(blank=True, upload_to='news/images/banners', verbose_name='Баннер'),
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='news/files/posts/%y/%m/%d', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='news/images/posts/%y/%m/%d', verbose_name='Изображение'),
        ),
    ]
