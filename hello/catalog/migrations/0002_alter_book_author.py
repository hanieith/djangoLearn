# Generated by Django 4.0 on 2022-02-19 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(help_text='Введите автора книги', to='catalog.Author', verbose_name='Автор книги'),
        ),
    ]
