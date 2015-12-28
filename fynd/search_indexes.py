import datetime
from haystack import indexes
from movieapi.models import Movie


class MovieIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    movie_name = indexes.CharField(model_attr='movie_name')
    director = indexes.CharField(model_attr='director')

    def get_model(self):
        return Movie

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

site.register(Movie, MovieIndex)
		 
