import requests


def get_wether(city_number):

   print(city_number)
   endpoint="https://weather.tsukumijima.net/api/forecast"
   respons=requests.get(endpoint+"/city/"+city_number)
   print(respons)
   respons_json=respons.json()

   weather_title=respons_json["title"]
   weather_location=respons_json["location"]
   weather_telop=respons_json["forecasts"][0]["telop"]
   weather_deta=respons_json["forecasts"][0]["date"]
   weather_image=respons_json["forecasts"][0]["image"]["url"]
   image = requests.get(weather_image).text
   weather_max=respons_json["forecasts"][0]["temperature"]["max"]["celsius"]
   weather_min=respons_json["forecasts"][0]["temperature"]["min"]["celsius"]

   context={
            "weather_title":weather_title,
            "weather_location":weather_location,
            "weather_telop":weather_telop,
            "weather_date":weather_deta,
            "weather_image":image,
            "weather_max":weather_max,
            "weather_min":weather_min,
        }
   
   return context

   


  
  
  
  
   # return respons_json



# dict_deta=respons.json()
# print(dict_deta["forecasts"][0]["date"]+dict_deta["forecasts"][0]["telop"])
# print(dict_deta["forecasts"][0]["temperature"]["max"]["celsius"])

if __name__ == "__main__":
   get_wether()