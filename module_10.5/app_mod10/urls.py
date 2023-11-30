from django.urls import path
from app_mod10 import views

urlpatterns = [
    path('',views.home),
    path('about/',views.about),
    path('catagory/',views.catagory),
    path('index/',views.index),

]
