# Generated by Django 4.0.3 on 2022-04-24 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0003_detailmodel_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailmodel',
            name='description',
            field=models.TextField(default='Описание', verbose_name='Описание'),
        ),
    ]
