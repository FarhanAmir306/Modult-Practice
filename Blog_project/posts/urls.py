from django.urls import path
from .import views

urlpatterns = [
    path('post/',views.add_post,name='add_post'),
    path('edit/<int:id>',views.edit_post,name='edit_post')
]
