# Generated by Django 4.1.1 on 2022-10-05 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_alter_category_options_alter_women_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='women',
            name='photo',
        ),
    ]
