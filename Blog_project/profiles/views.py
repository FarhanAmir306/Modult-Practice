from django.shortcuts import render,redirect
from .import forms
# Create your views here.
def add_profile(request):
    if request.method=='POST':
        form=forms.ProfileForm(request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()
            return redirect('add_profile')
    
    else:
        form=forms.ProfileForm()
    return render(request,'author.html',{'form':form})