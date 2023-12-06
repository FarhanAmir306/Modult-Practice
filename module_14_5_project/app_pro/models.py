from django.db import models
from django.utils import timezone

# Create your models here.
class CollageModel(models.Model):
    auto_field = models.AutoField(primary_key=True)
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255,default='hello')
    date_field = models.DateField()
    date_time_field = models.DateTimeField(default=timezone.now)
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
    email_field = models.EmailField()

    file_field = models.FileField(upload_to='app_pro/upload/',default='hello')
    file_path_field = models.FilePathField(path='app_pro/upload/',default='hello')
    float_field = models.FloatField()
    generic_ip_address_field = models.GenericIPAddressField()
    json_field = models.JSONField()
    positive_big_integer_field = models.PositiveBigIntegerField()
    text_field = models.TextField()
    time_field = models.TimeField()
    url_field = models.URLField()
    uuid_field = models.UUIDField()

 
