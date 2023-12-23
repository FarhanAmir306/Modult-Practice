# Generated by Django 4.2.7 on 2023-12-21 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0001_initial'),
        ('car', '0005_remove_brand_post_brand_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brand.brand'),
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
    ]