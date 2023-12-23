from django.urls import path
from . import views
urlpatterns = [
    path('Album/',views.add_album.as_view(),name='add_album'),
    path('editAlbum/<int:id>/',views.edit_album.as_view(),name='edit_album'),
    path('deleteAlbum/<int:id>/',views.delete_album.as_view(),name='delete_album'),
    
]
