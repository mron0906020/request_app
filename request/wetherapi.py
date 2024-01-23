import requests


def get_wether(city_number):

   print(city_number)
   endpoint="https://weather.tsukumijima.net/api/forecast"
   respons=requests.get(endpoint+"/city/"+city_number)
   print(respons)
   respons_json=respons.json()
   return respons_json
# dict_deta=respons.json()
# print(dict_deta["forecasts"][0]["date"]+dict_deta["forecasts"][0]["telop"])
# print(dict_deta["forecasts"][0]["temperature"]["max"]["celsius"])

if __name__ == "__main__":
   get_wether()