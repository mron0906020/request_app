from django.shortcuts import render,get_object_or_404

from .wetherapi import get_wether



def index(request):

    return render(request, 'request/index.html')

def detail(request):
    if "post" in request.method.lower():
        city_number=request.POST.get("location")
        print("city_number->",city_number)        
        weather=get_wether(city_number)
        weather_title=weather["title"]
        weather_date=weather["forecasts"]["date"]
        weather_forecasts=weather["forecasts"]
        weather_location=weather["location"]
        weather_image=weather["image"]
        
        context={
            "weather_title":weather_title,
            "weather_date":weather_date,
            "weather_forecasts":weather_forecasts,
            "weather_location":weather_location,
            "weather_image":weather_image,
        }

    return render(request, 'request/detail.html',context)

