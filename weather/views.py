from django.shortcuts import render
from django.http import request
from django.http import HttpResponse
# Create your views here.
def index(request):
    url='https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=4419e6fa99d3919e36dfeeda25467809'
    city='vijayawada'
    return render(request,'weather/weather.html')
    #return HttpResponse("Hello")