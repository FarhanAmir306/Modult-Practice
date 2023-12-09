from django.urls import  path 
from . import views
urlpatterns = [
    path('category/',views.add_category,name='category_link')
]
