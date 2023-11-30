from django.shortcuts import render
from datetime import datetime
# Create your views here.
def home(request):
    d={'name':'farhan',
       'age':23,
       'class':10,
        'list':[
           { 'name':'farhan','class':5,'section':'a'},
           { 'name':'amir','class':6,'section':'b'},
           { 'name':'sujon','class':7,'section':'c'},
        ],
        'section':'a',
        'text':"how are you. i'am ",
        'read': 'thank you',
        'birth':datetime.now(),
        'array':[1,2,3],
        'line':['a'],
        'string':'123',
        'slug':'This is an Example String!@#$',
        'post':datetime.now() ,
        'title':'<h1> my FIRST post </h1>',  
        
        }
    return render(request,'index.html',d)


def about(request):
    return render(request,'about.html')
def catagory(request):
    return render(request,'catagory.html')
def index(request):
    return render(request,'index.html')
