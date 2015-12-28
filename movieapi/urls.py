from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from movieapi import views

# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^genres/$',
        views.GenreList.as_view(),
        name='genre-list'),
     url(r'^genres/(?P<pk>[0-9]+)/movies/$',
        views.GenreDetail.as_view(),
        name='genre-detail'),
    url(r'^movie/(?P<pk>[0-9]+)/$',
        views.MovieDetail.as_view(),
        name='movie-detail'),
])

# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]