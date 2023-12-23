from django.db import models
from category.models import CatagoryModel
from authors.models import AuthorModel
# Create your models here.
class PostModel(models.Model):
    title=models.CharField( max_length=100)
    content=models.TextField()
    category=models.ManyToManyField(CatagoryModel,)
    author=models.ForeignKey(AuthorModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.title