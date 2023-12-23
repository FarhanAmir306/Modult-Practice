from django.urls import path
from .import views
app_name='author'
urlpatterns = [
    path('author/',views.add_author,name='add_author')
]
