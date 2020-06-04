from django.shortcuts import render
from django.http import request
from . models import City
import requests
from. forms import CityForm
from .  models import City
from django.shortcuts import render
# Create your views here.
def index(request):
    url='https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=4419e6fa99d3919e36dfeeda25467809'

    if request.method=='POST':
        form=CityForm(request.POST)
        form.save()

    form=CityForm

    weather_data=[]
    cities=City.objects.all()
    for city in cities:
        r=requests.get(url.format(city)).json()
        city_weather={
        'city' : city.name,
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)

    context={'city_weather':weather_data,'form':form}

    return render(request,'weather/weather.html',context)
