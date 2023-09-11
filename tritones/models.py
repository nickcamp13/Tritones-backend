from django.db import models

# Create your models here.
class TritoneSpotifyTrack(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    year_released = models.CharField(max_length=255)
    spotify_id = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name