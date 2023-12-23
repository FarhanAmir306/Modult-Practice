from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/',views.RegisterView.as_view(),name='register'),
    path('edit/',views.ProfileUpdate.as_view(),name='edit'),
    path('login/', views.MyLoginView.as_view(),name='login'),
    path('logout/', views.LogoutView.as_view(),name='logout'),
    path('car/<int:id>/', views.CarDetailView.as_view(), name='cardetails'),
    path('', views.category, name='homepage'),
    path('category/<slug:category_slug>/', views.category, name='category_wise_post'),
    path('buy/<int:id>/', views.car_buy, name='buy'),
    path('profile/', views.profile, name='profile'),
    # path('edit/', views.profile_update, name='edit'), 
    # path('show/', views.show.as_view(), name='show'), 



]



