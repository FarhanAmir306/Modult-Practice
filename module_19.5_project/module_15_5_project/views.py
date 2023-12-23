from django.shortcuts import render
from Album.models import AlbumModel

def home(request):
    album_data=AlbumModel.objects.all()
    for i in album_data:
        print(i.Album_Name)
    return render(request,'home.html',{'album':album_data})