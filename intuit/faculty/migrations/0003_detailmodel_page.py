# Generated by Django 4.0.3 on 2022-04-24 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0002_pagesmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailmodel',
            name='page',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='faculty.pagesmodel', verbose_name='Страница'),
        ),
    ]
