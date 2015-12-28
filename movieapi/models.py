from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class Genre(models.Model):
    genre_name = models.CharField(max_length=100,unique=True)
	
    def __str__(self):
	    return self.genre_name
		
class Movie(models.Model):
    movie_name = models.CharField(max_length=200)
    imdb_score = models.FloatField()
    popularity_99 = models.FloatField()
    director = models.CharField(max_length=200)
    image = models.URLField(max_length=300)
    genres = models.ManyToManyField(Genre,related_name = 'movies')
    date = models.DateTimeField(default=datetime.now)
	
    def __str__(self):
	    return self.movie_name