from django.urls import path
from .import views

urlpatterns = [
    # path('category/',views.add_category,name='add_category'),
    path('details/<int:id>/', views.DetailPostView.as_view(), name='details_post'),
    # path('post/',views.add_post,name='add_post'),
    path('post/',views.AddCreateView.as_view(),name='add_post'),
    # path('edit/<int:id>',views.edit_post,name='edit_post'),
    path('edit/<int:id>/',views.UpadatePost.as_view(),name='edit_post'),
    # path('delete/<int:pk>',views.delete_post,name='delete_post'),
    # path('delete/<int:pk>/',views.Delete_Post.as_view(),name='delete_post'),
    # path('details/<int:id>/',views.Details_Post.as_view(),name='details_post'),
    path('pay/<int:id>/',views.pay,name='paymoney'),
    path('comments/<int:pk>/',views.PostView.as_view(),name='comment'),
    
]
