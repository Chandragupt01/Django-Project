from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializers
from .models import Movies

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset=Movies.objects.all()
    serializer_class=MovieSerializers

class ActionViewSet(viewsets.ModelViewSet):
    queryset=Movies.objects.filter(typ='action')
    serializer_class=MovieSerializers

class ComedyViewSet(viewsets.ModelViewSet):
    queryset=Movies.objects.filter(typ='comedy')
    serializer_class=MovieSerializers