from typing import Any
from django.shortcuts import render,redirect
from .import forms
from .import models
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView,UpdateView,DetailView
from django.urls import reverse_lazy
from posts.models import Post 
from accounts.models import UserAccount
from django.shortcuts import get_object_or_404
from django.views import View
from django.utils.decorators import method_decorator

from django.contrib.auth.mixins import LoginRequiredMixin


# def add_category(request):
#     if request.method=='POST':
#         form=forms.CategoryForm(request.POST)
#         if form.is_valid():
#             print(request.POST)
#             form.save()
#             return redirect('add_category')
    
#     else:
#         form=forms.CategoryForm()
#     return render(request,'category.html',{'form':form})



class AddCreateView(CreateView,LoginRequiredMixin):
    model=models.Post
    form_class=forms.PostForm
    template_name = 'posts.html'
    success_url=reverse_lazy('add_post')

    def form_valid(self, form):
        form.instance.authors = self.request.user
        messages.success(self.request, "The Post was created successfully.")
        return super().form_valid(form)
    


class UpadatePost(UpdateView,LoginRequiredMixin):
    model=models.Post
    form=forms.PostForm
    template_name = 'delet.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('homepage')

    def form_valid(self, form):
        messages.success(self.request, "The Post was Update successfully.")
        return super().form_valid(form)
    

# class Delete_Post(DeleteView):
#     model=models.Post
#     form=forms.PostForm
#     pk_url_kwarg='id'
#     template_name='delet.html'
#     success_url=reverse_lazy('homepage')


class DetailPostView(DetailView,LoginRequiredMixin):
    model = models.Post
    pk_url_kwarg = 'id'
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object # post model er object ekhane store korlam
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context



class PostView(View,LoginRequiredMixin):
    template_name = 'comment_form.html'

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        # comments = post.comments.all()
        comment_form = forms.CommentForm()
        return render(request, self.template_name, {'comment_form': comment_form})

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            
        return self.get(request, *args, **kwargs)


def pay(request, id):
    user_account = get_object_or_404(UserAccount, user=request.user)
    post = get_object_or_404(Post, id=id)

    if post.is_paid:
        messages.error(request, "You have already paid for this book.")
    else:
        book_price = post.price
        user_account.balance += book_price
        user_account.save(update_fields=["balance"])
        post.is_paid = True
        post.save(update_fields=["is_paid"])
        messages.success(request, "Payment successful!")
    return redirect('profile')

