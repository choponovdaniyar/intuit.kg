# Generated by Django 4.0.3 on 2022-04-22 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_filemodel_file_alter_imagemodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='Ссылка'),
        ),
    ]
