# Generated by Django 4.0.3 on 2022-05-03 07:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_choiceprogram_date_alter_choiceprogram_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('logo', models.FileField(upload_to='main/partners/logo/', verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'Партнер',
                'verbose_name_plural': 'Партнеры',
                'ordering': ('title',),
            },
        ),
        migrations.AlterField(
            model_name='choiceprogram',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 3, 13, 52, 11, 752844), verbose_name='Дата регистрации'),
        ),
        migrations.AlterField(
            model_name='interesusermodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 3, 13, 52, 11, 752844), verbose_name='Дата регистрации'),
        ),
    ]
