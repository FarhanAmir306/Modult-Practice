from django.shortcuts import render,redirect
from .forms import TaskForm 
from .models import TaskModel
# Create your views here.
def add_task(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            # return render(request,'task.html',{'form':form})
            return redirect('task_link')
        
    else:
        form=TaskForm()
    return render(request,'task.html',{'form':form})


def edit_task(request,id):
    post_model=TaskModel.objects.get(pk=id)
    post_form=TaskForm(instance=post_model)
    if request.method=='POST':
        post_form=TaskForm(request.POST,instance=post_model)
        if post_form.is_valid():
            post_form.save()
            return redirect('show_task')
    
    return render(request,'task.html',{'form':post_form})

def delete_task(request,id):
    post=TaskModel.objects.get(pk=id)
    print(post)
    post.delete()
    return redirect('show_task')
