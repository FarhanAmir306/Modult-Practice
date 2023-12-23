from django.db import models

# Create your models her

class Brand(models.Model):
    brand_name=models.CharField(max_length=100)
    