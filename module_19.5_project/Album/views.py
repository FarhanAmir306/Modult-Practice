from django.shortcuts import render,redirect
from .import forms
from .import models
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required,name='dispatch')
class add_album(CreateView):
    model =models.AlbumModel
    form_class=forms.AlbumForm
    template_name='album.html '
    success_url = reverse_lazy('add_album')
    
   
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(add_album,self).form_valid(form)
    

@method_decorator(login_required,name='dispatch')
class edit_album(UpdateView):
    model = models.AlbumModel
    form_class=forms.AlbumForm
    template_name='album.html'
    success_url = reverse_lazy('add_album')
    pk_url_kwarg='id'
    
    def form_valid(self, form):
        messages.success(self.request, "The task was updated successfully.")
        return super(edit_album,self).form_valid(form)
    




# def delete_album(request,id):
#     post=models.AlbumModel.objects.get(pk=id)
#     post.delete()
#     return redirect('add_album')
    
    

    
@method_decorator(login_required ,name='dispatch')

class delete_album(DeleteView):
    model = models.AlbumModel
    pk_url_kwarg = 'id'
    template_name = 'del.html'
    success_url = reverse_lazy('homepage')
 
    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(delete_album, self).form_valid(form)