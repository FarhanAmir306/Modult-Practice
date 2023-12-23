from django.db import models

# Create your models here.
class MusicianModel(models.Model):
    First_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Phone=models.CharField(max_length=15)
    Instrument_Type=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.First_Name
    