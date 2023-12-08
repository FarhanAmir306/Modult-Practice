from django.shortcuts import render,redirect
from .import forms
from .import models
# Create your views here.
def add_album(request):
    if request.method == 'POST':
        form=forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            return redirect('add_album')
        
    else:
        form=forms.AlbumForm()
    return render(request,'album.html',{'form':form})


def edit_album(request,id):
    post_model=models.AlbumModel.objects.get(pk=id)
    post_form=forms.AlbumForm(instance=post_model)
    if request.method == 'POST':
        post_form=forms.AlbumForm(request.POST,instance=post_model)
        if post_form.is_valid():
            post_form.save()
            print(request.POST)
            return redirect('add_album') 
    return render(request,'album.html',{'form':post_form})


def delete_album(request,id):
    post=models.AlbumModel.objects.get(pk=id)
    post.delete()
    return redirect('add_album')