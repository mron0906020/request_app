from django.shortcuts import render,get_object_or_404

from .wetherapi import get_wether








def index(request):

    return render(request, 'request/index.html')

def detail(request):
    city_number=request.POST["location"]
    print("city_number->",city_number)        
    weather=get_wether(city_number)
    context={
        "weather":weather
    }
    return render(request, 'request/detail.html',context)


        # weather_title=weather["title"]
        # weather_forecasts=weather["forecasts"]
        # weather_location=weather["location"]
        # weather_image=weather["forecasts"][0]["image"]["url"]
        # image = requests.get(weather_image).text


        
        # context={
        #     "weather_title":weather_title,
        #     "weather_forecasts":weather_forecasts,
        #     "weather_location":weather_location,
        #     "weather_image":image,
        # }