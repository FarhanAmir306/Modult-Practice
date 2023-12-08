from django.shortcuts import render,redirect
from .forms import MusicianForm
from .import models
# Create your views here.

def add_musician(request):
    if request.method=='POST':
        form =MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            return redirect('add_musician')

    else:
        form=MusicianForm()
    return render(request,'music.html',{'form':form})


def edit_musician(request,id):
    post_model=models.MusicianModel.objects.get(pk=id)
    post_form=MusicianForm(instance=post_model)
    if request.method=='POST':
        form =MusicianForm(request.POST,instance=post_model)
        if form.is_valid():
            form.save()
            print(request.POST)
            return redirect('add_musician')
        
    return render(request,'music.html',{'form':post_form})