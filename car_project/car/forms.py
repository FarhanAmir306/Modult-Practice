from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from . import models


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    first_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name' ,'email', 'password1', 'password2', )


class UserChange(UserChangeForm):
    password=None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class CarForm(forms.ModelForm):
    class Meta:
        model=models.Car
        fields='__all__'




class CommentForm(forms.ModelForm):
    class Meta: 
        model = models.Comment
        fields = ['name', 'email', 'body']