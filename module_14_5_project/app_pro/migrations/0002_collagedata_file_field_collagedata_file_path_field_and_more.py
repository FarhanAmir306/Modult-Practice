# Generated by Django 4.2.7 on 2023-12-05 16:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_pro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collagedata',
            name='file_field',
            field=models.FileField(default='hello', upload_to='files/upload/'),
        ),
        migrations.AddField(
            model_name='collagedata',
            name='file_path_field',
            field=models.FilePathField(default='hello', path='/path/to/files/G:\\wallpaper'),
        ),
        migrations.AlterField(
            model_name='collagedata',
            name='char_field',
            field=models.CharField(default='hello', max_length=255),
        ),
        migrations.AlterField(
            model_name='collagedata',
            name='date_time_field',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
