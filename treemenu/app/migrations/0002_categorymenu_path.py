# Generated by Django 4.2.7 on 2023-11-06 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymenu',
            name='path',
            field=models.SlugField(blank=True, max_length=500, null=True, verbose_name='Элемент пути'),
        ),
    ]
