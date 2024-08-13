from django.shortcuts import render,HttpResponse
import requests
import datetime

# Create your views here.
def home(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'pune'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e9a48c8beb9f704abbe024e9f9c6d2a4'
    PARAMS = {'units':'metric'}

    data=requests.get(url,params=PARAMS).json()
    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']

    day = datetime.date.today()

    return render(request,'weatherapp/index.html',{'description':description,'icon':icon,'temp':temp,'day':day,'city':city})