from rest_framework import serializers
from .models import Movies

class MovieSerializers(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model=Movies
        fields = ['id','name','duration','rating','typ','image']