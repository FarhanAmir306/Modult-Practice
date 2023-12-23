from django import forms
from . import models
class BrandForm(forms.ModelForm):
    class Meta:
        models=models.Brand
        fields=['brand_name']