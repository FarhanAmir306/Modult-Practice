from django import forms 
from .models import MusicianModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MusicianForm(forms.ModelForm):
    class Meta:
        model=MusicianModel
        fields='__all__'
        


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username',  'email', 'password1', 'password2', )

