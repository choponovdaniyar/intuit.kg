# Generated by Django 4.0.3 on 2022-04-22 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_filemodel_file_alter_imagemodel_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='status',
            field=models.CharField(choices=[('active', 'активен'), ('passive', 'не активен')], default='passive', max_length=15, verbose_name='Статус'),
        ),
    ]
