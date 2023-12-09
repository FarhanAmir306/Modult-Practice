from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    Category_Name=models.CharField(max_length=200)
    

    def __str__(self) -> str:
        return self.Category_Name