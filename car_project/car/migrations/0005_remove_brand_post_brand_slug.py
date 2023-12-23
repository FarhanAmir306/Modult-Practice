# Generated by Django 4.2.7 on 2023-12-21 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_remove_comment_post_comment_car'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='post',
        ),
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]