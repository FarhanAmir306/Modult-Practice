from django.db import models

from django.contrib.auth.models import User
from accounts.models import UserAccount


# Create your models here.

class CatagoryModel(models.Model):
    name=models.CharField(max_length=20)
    slug=models.SlugField(max_length=100,null=True)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    author=models.ForeignKey(UserAccount,related_name='authors', on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField( max_length=100)
    bookname=models.CharField(max_length=100,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    category=models.ManyToManyField(CatagoryModel)
    price = models.DecimalField(
        max_digits=10,  
        decimal_places=2,  
        default=0.00,  
    )
    image=models.ImageField(upload_to='posts/media/uploads/',null=True,blank=True)
    is_paid = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    

class Comment_Post(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments',null=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Comments by {self.name}"
        



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    book_post = models.ManyToManyField(Post)
    


