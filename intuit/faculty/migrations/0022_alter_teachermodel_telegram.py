# Generated by Django 4.0.3 on 2022-05-11 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0021_alter_teachermodel_telegram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachermodel',
            name='telegram',
            field=models.SlugField(blank=True, help_text='Введите ссылку на профиль (не обязательное полое)<br>Номер тефона с кодом страны c плюсиком', verbose_name='Телеграм'),
        ),
    ]