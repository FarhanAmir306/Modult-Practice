from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('register/',views.user_register,name='register_link'),
    path('login/',views.user_login,name='login_link'),
    path('profile/',views.edit_profile,name='edit_profile'),
    path('password/',views.ChangeUserPassword,name='changepassword'),
    path('password2/',views.ChangeUserPassword2,name='changepassword2'),
    path('logout/',views.user_logout,name='logout'),

]
