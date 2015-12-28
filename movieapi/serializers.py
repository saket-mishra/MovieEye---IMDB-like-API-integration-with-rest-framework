from rest_framework import serializers
from movieapi.models import Movie,Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('url','id','genre_name','movies')

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True,read_only=True)
    class Meta:
        model = Movie
        fields = ('url','id','movie_name','imdb_score','popularity_99','director','image','genres')