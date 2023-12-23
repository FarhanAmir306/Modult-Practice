from django import forms 
from .models import AuthorModel

class AuthorForm(forms.ModelForm):
    class Meta:
        model=AuthorModel
        fields='__all__'