from django.shortcuts import render,redirect
from .import forms 
# Create your views here.
def add_category(request):
    if request.method=='POST':
        form=forms.CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            # return render(request,'category.html',{'form':form})
            return redirect('category_link')
        
    else:
        form=forms.CategoryForm()
    return render(request,'category.html',{'form':form})