# Generated by Django 4.0.3 on 2022-05-11 04:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_choiceprogram_date_alter_interesusermodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choiceprogram',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 11, 10, 8, 55, 470097), verbose_name='Дата регистрации'),
        ),
        migrations.AlterField(
            model_name='interesusermodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 11, 10, 8, 55, 470097), verbose_name='Дата регистрации'),
        ),
    ]
