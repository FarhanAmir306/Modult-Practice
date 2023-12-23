from django.urls import path 
from .import views

urlpatterns = [
    path('music/',views.add_musician.as_view(),name='add_musician'),
    path('edit/<int:id>/',views.edit_musician.as_view(),name='edit_musician'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('logout/',views.UserLogoutView.as_view(),name='logout'),
    path('signup/',views.RegisterView.as_view(),name='signup'),
]
