from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse

from wetherapi import get_wether

from .models import Weather


def index(request):

    return render(request, 'request_app/index.html')

def detail(request):
    if "post" in request.method.lower():
        city_number=request.POST.get()
        print("city_number->",city_number)
        
        weather=get_wether(city_number)
        weather_forecasts=weather["forecasts"]
        weather_location=weather["location"]
        weather_image=weather["image"]

        context={
            "nessage":"welcome my API test",
            "weather_forecasts":weather_forecasts,
            "weather_location":weather_location,
            "weather_image":weather_image,
        }

    return render(request, 'request_app/detail.html',context)

