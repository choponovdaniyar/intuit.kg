# Generated by Django 4.0.3 on 2022-04-24 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0011_remove_detailmodel_documents_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='details',
            field=models.ManyToManyField(related_name='detail_profile', to='faculty.detailmodel', verbose_name='Детали'),
        ),
    ]
