from django.urls import path
from .import views
app_name='meals_app'
urlpatterns = [
    path('show/iteam/',views.show,name='show'),
]
