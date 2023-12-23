from django.shortcuts import render
from posts.models import PostModel

def home(request):
    data=PostModel.objects.all()
    return render (request,'home.html',{'data':data})