from django.shortcuts import render
from .form import StudentData,CollageForm

# Create your views here.
def form_api(request):
    if request.method=='POST':
        form=StudentData(request.POST,request.FILES)
        if form.is_valid():
            file=form.cleaned_data['file']
            with open('./app_pro/upload/' + file.name,'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            print(form.cleaned_data)
            return render(request,'./app_pro/form_api.html',{'form':form})
    else:
        form=StudentData()
    return render(request,'./app_pro/form_api.html',{'form': form})


def model_form(request):
    if request.method=='POST':
        data = CollageForm(request.POST)
        if data.is_valid():
           print(data.cleaned_data)
           return render(request,'./app_pro/model_form.html',{'data':data})
    
    else:
        data=CollageForm()
    return render(request,'./app_pro/model_form.html',{'data':data})
  
