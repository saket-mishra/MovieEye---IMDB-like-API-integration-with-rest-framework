from django.shortcuts import render
from movieapi.models import Genre,Movie
from movieapi.serializers import GenreSerializer,MovieSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticatedOrReadOnly

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'genres': reverse('genre-list', request=request, format=format)
    })

class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
         genres = Genre.objects.get(pk=self.kwargs.get('pk',None))
         movies = Movie.objects.filter(genres=genres)
         return movies

class GenreList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_object(self):
        movie_id = self.kwargs.get('pk',None)
        return Movie.objects.get(pk=movie_id) 
