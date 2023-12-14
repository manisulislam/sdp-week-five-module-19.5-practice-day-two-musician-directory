from django.db import models
from musician.models import musicianModel
# Create your models here.
class addAlbumModel(models.Model):
    AlbumName = models.CharField(max_length=100)
    release_date=models.DateTimeField(auto_now_add=True)
    rating_choices=( 
    ("1", "1"), 
    ("2", "2"), 
    ("3", "3"), 
    ("4", "4"), 
    ("5", "5"), 
    
) 
    ratings=models.CharField(choices=rating_choices, max_length=1)
    musician=models.ForeignKey(musicianModel,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.AlbumName