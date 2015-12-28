from django.conf.urls import patterns, include, url
from imgui import views


urlpatterns = [
    url(r'^$', views.genres, name="genre_list"),
    url(r'^genres/(?P<id>\d+)/movies/$', views.movielist, name="movies_list"),
    url(r'^movie/(?P<id>\d+)/$', views.moviedetail, name="movies_detail"),
    url(r'^popular-movies/$', views.popularity, name="popular"),
    url(r'^highest-rated-movies/$', views.score, name="rating"),
    
]