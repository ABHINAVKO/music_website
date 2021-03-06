from django.db import models

# Create your models here.

class Album(models.Model):
    artist=models.CharField(max_length=250)
    album_title=models.CharField(max_length=600)
    genre=models.CharField(max_length=90)
    album_logo=models.CharField(max_length=2000)

    def __str__(self):
        return self.album_title +':'+self.artist

class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=20)
    song_title=models.CharField(max_length=225)
    is_favorite=models.BooleanField(default=False)

    def __str__(self):
        return self.song_title