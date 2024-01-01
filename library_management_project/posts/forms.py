from django import forms 
from .models import Post ,Comment_Post,CatagoryModel
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=('is_paid',)
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment_Post
        fields = ['name', 'email', 'body']


class CategoryForm(forms.ModelForm):
    class Meta:
        model=CatagoryModel
        fields='__all__'

