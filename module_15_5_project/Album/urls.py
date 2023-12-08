from django.urls import path
from . import views
urlpatterns = [
    path('Album/',views.add_album,name='add_album'),
    path('editAlbum/<int:id>/',views.edit_album,name='edit_album'),
    path('deleteAlbum/<int:id>/',views.delete_album,name='delete_album'),
    
]
