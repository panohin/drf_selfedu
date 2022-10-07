# Generated by Django 4.1.1 on 2022-10-03 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название категории')),
            ],
        ),
        migrations.CreateModel(
            name='Women',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Загловок')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Контент')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фотография')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('is_published', models.BooleanField(default=False, verbose_name='Черновик')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='women.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Известные женщины',
                'verbose_name_plural': 'Известная женщинаs',
                'ordering': ['-time_create'],
            },
        ),
    ]
