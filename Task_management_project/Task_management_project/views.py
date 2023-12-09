from django.shortcuts import render
from task.models import TaskModel


def home(request):
    return render (request,'base.html')


def show_task(request):   
    data=TaskModel.objects.all()
    return render(request,'show.html',{'data':data})