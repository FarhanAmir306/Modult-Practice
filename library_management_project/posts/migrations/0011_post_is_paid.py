# Generated by Django 5.0 on 2023-12-31 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
