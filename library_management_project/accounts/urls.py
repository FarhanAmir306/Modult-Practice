from django.urls import path
from .views import UserRegistrationView, UserLoginView, logout_view,UserBankAccountUpdateView,BookBuy,profile

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),

    path('logout/',logout_view, name='logout'),
    path('profile_information/', UserBankAccountUpdateView.as_view(), name='profile_information'),
    # path('profile/',ProfileView.as_view(), name='profile'),
    path('profile/',profile, name='profile'),
    path('buy/<int:id>/',BookBuy,name='bookbuy'),
    
]