import requests
from django.shortcuts import render,redirect
from .models import City
from .forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=Metric&appid=4419e6fa99d3919e36dfeeda25467809'
    err_msg=''
    message=''
    message_class='is-danger'
    if request.method=='POST':
        form=CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name'].upper()
            nc_count=City.objects.filter(name=new_city).count()
            if nc_count==0:
                r = requests.get(url.format(new_city)).json()

                if r['cod']==200:
                    form.save()
                else:
                    err_msg="City doesnt exists Try with Some other city."
            else:
                err_msg = "City already exists !"

        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = "City added succesfully !"
            message_class = 'is-success'

    print(err_msg)
    form=CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)

    context = {'weather_data' : weather_data,
               'form' : form,
               'message':message,
               'message_class' : message_class
               }
    return render(request, 'weather/weather.html', context)

def delete_city(request,city_name):
    City.objects.get(name=city_name).delete()
    return redirect('home')