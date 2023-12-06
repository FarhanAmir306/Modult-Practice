from django.urls import path
from .import views
urlpatterns = [
    path('form_api/',views.form_api,name='form_api'),
    path('model_form/',views.model_form,name='model_form'),
]
