from typing import Any
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from .models import Car, Profile
from brand.models import Brand
from . import forms
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import FormView ,UpdateView
from django.contrib.auth import login 
from .forms import RegisterForm
from django.contrib.auth.views import LoginView 
from django.views.generic.detail import DetailView 
from django.contrib.auth import logout
from django.views.generic import View
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class RegisterView(FormView):
    template_name = 'account.html'
    form_class = RegisterForm
    success_url = reverse_lazy('homepage')
    
    def form_valid(self, form):
        user = form.save()
        messages.success(self.request,'Register Successfully !')
        if user:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Register'
        return context
    


@method_decorator(login_required,name='dispatch')

class ProfileUpdate(UpdateView):
    model = User
    form_class=forms.UserChange
    # fields = ['username','first_name','last_name']
    template_name='edit_profile.html'
    success_url = reverse_lazy('homepage')
    
    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "The task was updated successfully.")
        return super(ProfileUpdate,self).form_valid(form)
    

    

# def profile_update(request):
#     if request.method == 'POST':
#         form = forms.UserChange(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('homepage')
#     else:
#         form = forms.UserChange(instance=request.user)

#     return render(request, 'edit_profile.html', {'form': form})
    


@login_required
def profile(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)
    cars = user_profile.cars.all()
    return render(request, 'profile.html', {'cars': cars})
  

class MyLoginView(LoginView):
    template_name = 'account.html'
    
    def get_success_url(self):
        return reverse_lazy('homepage') 
    
    def form_valid(self, form):
        messages.success(self.request, 'Login successful!')
        return super().form_valid(form)
    
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
@method_decorator(login_required,name='dispatch')
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(self.request, 'Logout successful!')
        return redirect('homepage')




def category(request, category_slug=None):
    cars = Car.objects.all()
    brands = Brand.objects.all()
    print(category_slug)
    if category_slug is not None:
        # brands = Brand.objects.get(brand_name=category_slug)
        cars = Car.objects.filter(brand__brand_name=category_slug)
        brand=Brand.objects.get(brand_name=category_slug)
        cars=Car.objects.filter(brand=brand)
    return render(request, 'home.html', {'cars': cars, 'brands': brands})
    

@method_decorator(login_required,name='dispatch')
class CarDetailView(DetailView):
    model = Car
    template_name='car_details.html'
    pk_url_kwarg='id'


    def post(self,request,*args,**kwargs):
        comment_form=forms.CommentForm(data=self.request.POST)
        car=self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.get_object()
        comments = car.comments.all()  
        comment_form = forms.CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context



@login_required
def car_buy(request,id):
    car=Car.objects.filter(id=id).first()
    car.quantity=car.quantity-1
    car.save()
    user_profile, created = Profile.objects.get_or_create(user=request.user)
    user_profile.cars.add(car)
    return redirect('profile')
   



    








