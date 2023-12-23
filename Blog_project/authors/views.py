from django.shortcuts import render,redirect
from .import forms
# Create your views here.
def add_author(request):
    if request.method=='POST':
        form=forms.AuthorForm(request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()
            return redirect('author:add_author')
    
    else:
        form=forms.AuthorForm()
    return render(request,'author.html',{'form':form})