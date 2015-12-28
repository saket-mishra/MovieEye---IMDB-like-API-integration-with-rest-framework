from django.shortcuts import render
import json
from django import template
import requests
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django import template
from movieapi.models import Genre,Movie
from django.conf import settings


def genres(request):
    data = requests.get('https://fyndapi.herokuapp.com/movieapi/genres/').json()
    set = Movie.objects.order_by('-date')[:8]
    context = RequestContext(request, {
        'gen': data,'set':set,
    }) 
    return render_to_response('imgui/genres.html', context)
	
def movielist(request,id):
    data = requests.get('https://fyndapi.herokuapp.com/movieapi/genres/' + id + '/movies/').json()
    count=len(data)
    context = RequestContext(request, {
        'genlist': data,'count':count,
    }) 
    return render_to_response('imgui/genrelist.html', context) 
	
def moviedetail(request,id):
    data = requests.get('https://fyndapi.herokuapp.com/movieapi/movie/' + id + '/').json()
    context = RequestContext(request, {
        'genlist': data,'gen': data['genres'],
    }) 
    return render_to_response('imgui/moviedetail.html', context) 
	
def popularity(request):
    data = Movie.objects.order_by('-popularity_99')
    count=len(data)
    context = RequestContext(request, {
        'm_list': data, 'count':count,
    }) 
    return render_to_response('imgui/display_pop.html', context) 

def score(request):
    data = Movie.objects.order_by('-imdb_score')
    count=len(data)
    context = RequestContext(request, {
        'm_list': data,'count':count
    }) 
    return render_to_response('imgui/display_rat.html', context) 