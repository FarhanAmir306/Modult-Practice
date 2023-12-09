from django.urls import  path 
from . import views
urlpatterns = [
    path('task/',views.add_task,name='task_link'),
    path('edit/<int:id>/',views.edit_task,name='edit'),
    path('delete/<int:id>/',views.delete_task,name='del_task'),
 
]
