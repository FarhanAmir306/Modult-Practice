from django.db import models
from authors.models import AuthorModel
# Create your models here.
class ProfileModel(models.Model):
    name=models.CharField(max_length=30)
    about=models.TextField()
    author=models.OneToOneField(AuthorModel,on_delete=models.CASCADE)


    def __str__(self):
        return self.name