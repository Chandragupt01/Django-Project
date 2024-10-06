from django.shortcuts import render
from . models import Movies
# Create your views here.

def movie_list(request):
    movie_object=Movies.objects.all()
    return render(request,'newapp/movie_list.html',{'movie_object':movie_object})