from django.shortcuts import render,redirect
from .import forms
from .import models
# Create your views here.
def add_post(request):
    if request.method=='POST':
        form=forms.PostForm(request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()
            return redirect('add_post')
    
    else:
        form=forms.PostForm()
    return render(request,'author.html',{'form':form})


def edit_post(request,id):
    post_model=models.PostModel.objects.get(pk=id)
    post_form =forms.PostForm(instance=post_model)
    if request.method=='POST':
        form=forms.post_form(request.POST,instance=post_model)
        if form.is_valid():
            print(request.POST)
            form.save()
            return redirect('homepage')
    
    else:
        form=forms.PostForm()
    return render(request,'author.html',{'form':form})
    
    
def delete_post(request,id):
    del_post=models.PostModel.objects.get(pk=id)
    del_post.delete()
    return redirect('homepage')