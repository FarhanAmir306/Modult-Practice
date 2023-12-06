from django import forms
from .models import CollageModel
import datetime
class StudentData(forms.Form):
    name=forms.CharField(max_length=20,initial='Your name')
    email=forms.EmailField( label="Enter your email address",)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    agree = forms.BooleanField(initial=True)
    birth_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years =BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    day = forms.DateField(initial=datetime.date.today)
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)
    time = forms.DurationField()
    file = forms.FileField()
    filepath = forms.FilePathField('G:\wallpaper')
    IP = forms.GenericIPAddressField()
    RegexField = forms.RegexField(regex = "G.*s")
    URLField = forms.URLField()



class CollageForm(forms.ModelForm):
    class Meta:
        model=CollageModel
        fields ='__all__'
