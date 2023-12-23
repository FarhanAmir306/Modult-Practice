from django import forms 
from .models import ProfileModel
class ProfileForm(forms.ModelForm):
    class Meta:
        model=ProfileModel
        fields='__all__'
        