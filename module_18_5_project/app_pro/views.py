from django.shortcuts import render,redirect
from .import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm ,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.



def home(request):
    return render(request,'home.html')

def user_register(request):
    if request.method=='POST':
        form=forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Create Successful !')
            return redirect('register_link')
        else:
            messages.success(request,'Account Create Faild !')
    else:
        form=forms.RegisterForm()
    return render(request, 'register.html',{'form':form ,'type':'register'})
        

def user_login(request):
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            user_name=form.cleaned_data['username']
            user_pass=form.cleaned_data['password']
            user=authenticate(username=user_name,password=user_pass)
            if user is not None:
                messages.success(request, 'Logged in Successfully')
                login(request,user)
                return redirect('homepage')
            else:
                messages.warning(request, 'Login informtion incorrect')
                return redirect('register_link')
            
    else:
        form=AuthenticationForm()
    return render(request,'register.html',{'form':form, 'type':'login'})

            
        
@login_required
def edit_profile(request):
    if request.method=='POST':
        form=forms.ChangeUserData(request.POST,instacne=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Updated success !')
            return redirect('edit_profile')
        else:
            messages.success(request,'Account Updated Faild !')
    else:
        form=forms.ChangeUserData(instance=request.user)
    return render(request,'profile.html',{'form':form})


        
def ChangeUserPassword(request):
    if request.method=='POST':
        form =PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            update_session_auth_hash(request,form.user)
            form.save()
            messages.success(request, 'Password Change Successfully')
            return redirect('homepage')
        
    else:
        form=PasswordChangeForm(request.user)
    return render(request,'changepassword.html',{'form':form,'type':'Change Password With old ' })

def ChangeUserPassword2(request):
    if request.method=='POST':
        form =SetPasswordForm(request.user,request.POST)
        if form.is_valid():
            update_session_auth_hash(request, form.user)
            form.save()
            messages.success(request, 'Password Change without old password Successfully')
            return redirect('homepage')
        
    else:
        form=SetPasswordForm(request.user)
    return render(request,'changepassword.html',{'form':form ,'type':'Change Password'})


def user_logout(request):
    logout(request)
    messages.success(request, 'Logout Successfully')
    return redirect('homepage')