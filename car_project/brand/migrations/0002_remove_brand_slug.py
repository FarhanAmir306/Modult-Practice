# Generated by Django 4.2.7 on 2023-12-21 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='slug',
        ),
    ]
