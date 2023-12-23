from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.
from brand.models import Brand

    

class Car(models.Model):
    image = models.ImageField(upload_to ='car/media/') 
    carname=models.CharField(max_length=100)
    carprice=models.CharField(max_length=100)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    description=models.TextField(null=True,blank=True)


    def __str__(self):
        return self.carname
    
    
from django.contrib.auth.models import User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cars = models.ManyToManyField(Car)


    



class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments',null=True,blank=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments by {self.name}"