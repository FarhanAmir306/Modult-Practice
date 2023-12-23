from django.db import models
from musician.models import MusicianModel


# Create your models here.
class AlbumModel(models.Model):
    Album_Name = models.CharField(max_length=50)
    Musician = models.ForeignKey(MusicianModel, on_delete=models.CASCADE)
    Album_release_date = models.DateTimeField(auto_now_add=True)
    RATING = [
        (1, "1 stars"),
        (2, "2 stars"),
        (3, "3 stars"),
        (4, "4 stars"),
        (5, "5 stars"),
    ]
    Rating = models.IntegerField(choices=RATING)
