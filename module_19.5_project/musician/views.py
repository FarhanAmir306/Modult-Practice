from django.shortcuts import render,redirect

from .import models
from .import forms

from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.views.generic.edit import FormView
# Create your views here.


from django.contrib.auth.views import LoginView ,LogoutView
from django.urls import reverse_lazy
from django.contrib import messages

from django.views.generic.edit import CreateView ,UpdateView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class UserLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('homepage') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
    


class UserLogoutView(LogoutView):
    success_url = reverse_lazy('homepage')
# def user_logout(request):
#     logout(request)

    

class RegisterView(FormView):
    template_name = 'signup.html'
    form_class = RegisterForm
    success_url = reverse_lazy('homepage')
    
    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)
    

@method_decorator(login_required,name='dispatch')
class add_musician(CreateView):
    model = models.MusicianModel
    form_class=forms.MusicianForm
    template_name='music.html'
    success_url = reverse_lazy('add_musician')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(add_musician,self).form_valid(form)
    

@method_decorator(login_required,name='dispatch')
class edit_musician(UpdateView):
    model = models.MusicianModel
    form_class=forms.MusicianForm
    template_name='music.html'
    success_url = reverse_lazy('homepage')
    pk_url_kwarg='id'
    
    def form_valid(self, form):
        messages.success(self.request, "The task was updated successfully.")
        return super(edit_musician,self).form_valid(form)

