# Generated by Django 4.1.1 on 2022-10-05 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='women',
            options={'ordering': ['-time_create'], 'verbose_name': 'Известная женщина', 'verbose_name_plural': 'Известные женщины'},
        ),
        migrations.AlterField(
            model_name='women',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='women',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фотография'),
        ),
    ]
